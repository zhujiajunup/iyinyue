__author__ = 'Administrator'

import math
import operator


# 计算两两用户的相似度
def user_similarity(train):
    item_users = dict()  # 物品与用户的对应表
    for user, items in train.items():  # 遍历所有用户及相关物品
        for item in items.keys():  # 遍历物品
            if item not in item_users:
                item_users[item] = set()
            item_users[item].add(user)  # 将用户user添加都物品item的用户表中
    same_item_num = dict()  # 存储用户之间具有相同物品的个数矩阵
    # （same_item_num[u][v] = 2 表示用户u与用户v拥有两件相同的物品）
    user_item_num = dict()
    for item, users in item_users.items():
        for user in users:
            if user not in user_item_num:
                user_item_num[user] = 0
            user_item_num[user] += 1  # 统计用户所拥有的物品个数
            for v in users:
                if user == v:
                    continue
                if user not in same_item_num:
                    same_item_num[user] = dict()
                if v not in same_item_num[user]:
                    same_item_num[user][v] = 0
                same_item_num[user][v] += 1 / math.log(1 + len(user))  # 原公式为：same_item_num[user][v] += 1
                # 改进后的 same_item_num[user][v] += 1 / math.log(1 + len(user))
                # 降低热门物品对用户间的相似度影响
    similarity = dict()  # 存储用户相似度
    for user, related_user in same_item_num.items():
        for v, cuv in related_user.items():
            # 计算两两用户的相似度，计算公式 |N(u) & N(v)|/sqrt(|N(u)|| N(v)|)
            # 公式注释：
            #    N(i)表示用户i感兴趣的物品集合
            #    N(u) & N(v) 表示用户u和用户v共同感兴趣的物品集合
            #    |N(u) || N(v)|表示用户u和用户v的物品总数
            if user not in similarity:
                similarity[user] = dict()
            if v not in similarity[user]:
                similarity[user][v] = 0.0
            similarity[user][v] = cuv / math.sqrt(user_item_num[user] * user_item_num[v])
    return similarity


def user_similarity2(train):
    item_users = dict()  # 物品与用户的对应表
    for user, items in train.items():  # 遍历所有用户及相关物品
        for item in items.keys():  # 遍历物品
            if item not in item_users:
                item_users[item] = set()
            item_users[item].add(user)  # 将用户user添加都物品item的用户表中
    same_item_num = dict()  # 存储用户之间具有相同物品的个数矩阵
    # （same_item_num[u][v] = 2 表示用户u与用户v拥有两件相同的物品）
    user_item_num = dict()
    for item, users in item_users.items():
        for user in users:
            if user not in user_item_num:
                user_item_num[user] = 0
            user_item_num[user] += 1  # 统计用户所拥有的物品个数
            for v in users:
                if user == v:
                    continue
                if user not in same_item_num:
                    same_item_num[user] = dict()
                if v not in same_item_num[user]:
                    same_item_num[user][v] = 0
                same_item_num[user][v] += 1 / math.log(1 + len(user))  # 原公式为：same_item_num[user][v] += 1
                # 改进后的 same_item_num[user][v] += 1 / math.log(1 + len(user))
                # 降低热门物品对用户间的相似度影响
    similarity = dict()  # 存储用户相似度
    for user, related_user in same_item_num.items():
        for v, cuv in related_user.items():
            # 计算两两用户的相似度，计算公式 |N(u) & N(v)|/sqrt(|N(u)|| N(v)|)
            # 公式注释：
            #    N(i)表示用户i感兴趣的物品集合
            #    N(u) & N(v) 表示用户u和用户v共同感兴趣的物品集合
            #    |N(u) || N(v)|表示用户u和用户v的物品总数
            if user not in similarity:
                similarity[user] = dict()
            if v not in similarity[user]:
                similarity[user][v] = 0.0
            similarity[user][v] = cuv / math.sqrt(user_item_num[user] * user_item_num[v])
    return similarity


# userCF推荐算法
def recommend(user, train, similarity):
    rank = dict()
    interacted_items = train[user]  # 获取用户感兴趣物品集合
    items = similarity[user].items()
    for v, wuv in sorted(similarity[user].items(), key=operator.itemgetter(1),
                         reverse=True)[0:3]:
        for i, rvi in train[v].items():
            if i in interacted_items:
                continue
            if i not in rank:
                rank[i] = 0
            rank[i] += wuv * 1
    return rank

train = dict()
train['A'] = {'a': {1}, 'b': {1}, 'd': {1}}
train['B'] = {'a': {1}, 'c': {1}}
train['C'] = {'b': {1}, 'e': {1}}
train['D'] = {'c': {1}, 'd': {1}, 'e': {1}}
similarity = user_similarity(train)
print("相似度矩阵", similarity)
print("推荐", recommend('A', train, similarity))