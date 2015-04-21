__author__ = 'jjZhu'
import math
from user_action import UserCF


# 计算召回率
def recall(train, test, N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        similarity = UserCF.user_similarity(train)
        rank = UserCF.recommend(user, train, similarity)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += float(len(tu))
    return hit / all


# 计算准确率
# train：训练数据集
# test：测试数据集
# N：计算得出的N个物品
def precision(train, test, N):
    hit = 0
    all = 0
    for user in train.keys():
        tu = test[user]
        similarity = UserCF.user_similarity(train)
        rank = UserCF.recommend(user, train, similarity)
        for item, pui in rank:
            if item in tu:
                hit += 1
        all += float(N)
    return hit / all


# 计算覆盖率
def coverage(train, test, N):
    recommend_item_num = 0
    all_item_num = 0
    for user in train.keys():
        for item in train[user].keys():
            all_item_num += 1
        similarity = UserCF.user_similarity(train)
        rank = UserCF.recommend(user, train, similarity)
        recommend_item_num += len(rank)
    return recommend_item_num / all_item_num


# 计算新颖度
def popularity(train, test, N):
    item_popularity = dict()
    for user, items in train.items():
        for item in items.keys():
            if item not in item_popularity:
                item_popularity[item] = 0
            item_popularity[item] += 1
    ret = 0
    n = 0
    for user in train.keys():
        similarity = UserCF.user_similarity(train)
        rank = UserCF.recommend(user, train, similarity)  # 获取推荐物品
        for item, pui in rank:
            ret += math.log(1 + item_popularity[item])
            n += 1
    ret /= float(n)
    return ret

