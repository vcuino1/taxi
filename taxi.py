import gym
import random

env = gym.make('Taxi-v2')

# 学习率
alpha = 0.5
# 折扣因子
gamma = 0.9
# ε
epsilon = 0.05

# 初始化Q表
Q = {}
for s in range(env.observation_space.n):
    for a in range(env.action_space.n):
        Q[(s, a)] = 0


# 更新Q表
def update_q_table(prev_state, action, reward, nextstate, alpha, gamma):
    # maxQ(s',a')
    qa = max([Q[(nextstate, a)] for a in range(env.action_space.n)])
    # 更新Q值
    Q[(prev_state, action)] += alpha * (reward + gamma * qa - Q[(prev_state, action)])


# ε-贪婪策略选取动作
def epsilon_greedy_policy(state, epsilon):
    # 如果＜ε，随机选取一个另外的动作（探索）
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    # 否则，选取令当前状态下Q值最大的动作（开发）
    else:
        return max(list(range(env.action_space.n)), key=lambda x: Q[(state, x)])


# 训练5000个episode
for i in range(5000):
    r = 0
    # 初始化状态（env.reset()用于重置环境）
    state = env.reset()
    # 一个episode
    while True:
        # 输出当前agent和environment的状态（可删除）
        env.render()
        # 采用ε-贪婪策略选取动作
        action = epsilon_greedy_policy(state, epsilon)
        # 执行动作，得到一些信息
        nextstate, reward, done, _ = env.step(action)
        # 更新Q表
        update_q_table(state, action, reward, nextstate, alpha, gamma)
        # s ⬅ s'
        state = nextstate
        # 累加奖励
        r += reward
        # 判断episode是否到达最终状态
        if done:
            break
    # 打印当前episode的奖励
    print("[Episode %d] Total reward: %d" % (i + 1, r))
#测试100个数据
for i in range(100):
    r = 0
    # 初始化状态（env.reset()用于重置环境）
    state = env.reset()
    # 一个episode
    while True:
        # 输出当前agent和environment的状态（可删除）
        env.render()
        # 采用ε-贪婪策略选取动作
        action = epsilon_greedy_policy(state, epsilon)
        # 执行动作，得到一些信息
        nextstate, reward, done, _ = env.step(action)
        # 更新Q表
        update_q_table(state, action, reward, nextstate, alpha, gamma)
        # s ⬅ s'
        state = nextstate
        # 累加奖励
        r += reward
        # 判断episode是否到达最终状态
        if r>=0:
            break
             # 打印当前episode的奖励
    print("[Episode %d] Total reward: %d" % (i + 1, r))
env.close()
