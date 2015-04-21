__author__ = 'jjZhu'
import math
import operator
import sys


# 计算物品间的相似度
def item_similarity(train):
    user_num = dict()  # user_num[i]记录喜欢物品i的用户数
    user_sim_num = dict()   # user_item_num[i][j]记录同时喜欢物品i和j的用户数
    for user, items in train.items():  # 遍历数据集中的用户-物品
        for i in items:  # 遍历当前用户所喜欢的物品
            if i not in user_num:
                user_num[i] = 0
            user_num[i] += 1  # 喜欢物品i的用户数+1
            for j in items:
                if i not in user_sim_num:
                    user_sim_num[i] = dict()
                if j not in user_sim_num[i]:
                    user_sim_num[i][j] = 0
                if i == j:
                    continue
                user_sim_num[i][j] += 1
    similarity_mat = dict()
    for i, related_items in user_sim_num.items():
        for j, wij in related_items.items():
            if i not in similarity_mat:
                similarity_mat[i] = dict()
            if j not in similarity_mat[i]:
                similarity_mat[i][j] = 0
            # 计算两两物品间的相似度矩阵
            # 计算公式为wij = |N(i) & N(j)|/||N(i)| * |N(j)||
            # 其中|N(i) & N(j)|同时对物品i,j感兴趣的用户数量
            # ||N(i)| * |N(j)||代表对物品i,j感兴趣的用户数量的乘积
            similarity_mat[i][j] += wij / math.sqrt(user_num[i] * user_num[j])
    return auto_norm(similarity_mat)  # 矩阵归一化


# 第二中方法计算物品间的相似度
# 将活跃用户的影响度考虑进去
def item_similarity2(train):
    user_num = dict()  # user_num[i]记录喜欢物品i的用户数
    user_sim_num = dict()   # user_item_num[i][j]记录同时喜欢物品i和j的用户数
    for user, items in train.items():  # 遍历数据集中的用户-物品
        for i in items:  # 遍历当前用户所喜欢的物品
            if i not in user_num:
                user_num[i] = 0
            user_num[i] += 1  # 喜欢物品i的用户数+1
            for j in items:
                if i not in user_sim_num:
                    user_sim_num[i] = dict()
                if j not in user_sim_num[i]:
                    user_sim_num[i][j] = 0
                if i == j:
                    continue
                user_sim_num[i][j] += 1 / math.log(1 + len(items) * 1.0)  # 降低活跃用户的影响度
    similarity_mat = dict()
    for i, related_items in user_sim_num.items():
        for j, wij in related_items.items():
            if i not in similarity_mat:
                similarity_mat[i] = dict()
            if j not in similarity_mat[i]:
                similarity_mat[i][j] = 0
            # 计算两两物品间的相似度矩阵
            # 计算公式为wij = |N(i) & N(j)|/||N(i)| * |N(j)||
            # 其中|N(i) & N(j)|同时对物品i,j感兴趣的用户数量
            # ||N(i)| * |N(j)||代表对物品i,j感兴趣的用户数量的乘积
            similarity_mat[i][j] += wij / math.sqrt(user_num[i] * user_num[j])
    return auto_norm(similarity_mat)  # 矩阵归一化


# 第三中方法计算物品间的相似度
def item_similarity3(train, a):
    user_num = dict()  # user_num[i]记录喜欢物品i的用户数
    user_sim_num = dict()   # user_item_num[i][j]记录同时喜欢物品i和j的用户数
    for user, items in train.items():  # 遍历数据集中的用户-物品
        for i in items:  # 遍历当前用户所喜欢的物品
            if i not in user_num:
                user_num[i] = 0
            user_num[i] += 1  # 喜欢物品i的用户数+1
            for j in items:
                if i not in user_sim_num:
                    user_sim_num[i] = dict()
                if j not in user_sim_num[i]:
                    user_sim_num[i][j] = 0
                if i == j:
                    continue
                user_sim_num[i][j] += 1 / math.log(1 + len(items) * 1.0)  # 降低活跃用户的影响度
    similarity_mat = dict()
    for i, related_items in user_sim_num.items():
        for j, wij in related_items.items():
            if i not in similarity_mat:
                similarity_mat[i] = dict()
            if j not in similarity_mat[i]:
                similarity_mat[i][j] = 0
            # 计算两两物品间的相似度矩阵
            # 计算公式为wij = |N(i) & N(j)|/||N(i)|^(1-a) * |N(j)||^a
            # 其中|N(i) & N(j)|同时对物品i,j感兴趣的用户数量
            # ||N(i)| * |N(j)||代表对物品i,j感兴趣的用户数量的乘积
            similarity_mat[i][j] += wij / (math.pow(user_num[i], 1 - a) * math.pow(user_num[j], a))
    return auto_norm(similarity_mat)  # 矩阵归一化


# 矩阵归一化
def auto_norm(mat):
    min_values = dict()
    max_values = dict()
    ranges = dict()
    norm_mat = dict()
    for i, items in mat.items():
        # min_values[i] = sys.maxsize
        # max_values[i] = 0
        # for j, wij in items.items():
        min_values[i] = min(items.items(), key=lambda d: d[1])[1]
        max_values[i] = max(items.items(), key=lambda d: d[1])[1]
        ranges[i] = max_values[i] - min_values[i]
    for i, items in mat.items():
        for j, wij in items.items():
            if i not in norm_mat:
                norm_mat[i] = dict()
            norm_mat[i][j] = (mat[i][j] - min_values[i]) / ranges[i]
    return norm_mat


def recommendation(train, user_id, similarity_mat, K):
    rank = dict()
    history_item = train[user_id]  # 获取用户历史喜欢物品
    for i, pi in history_item.items():
        for j, wj in sorted(similarity_mat[i].items(),  # 获取相似物品并降序排序
                            key=operator.itemgetter(1), reverse=True)[0:K]:
            if j in history_item:  # 如果待推荐物品在该用户的历史物品中已出现，则不推荐
                continue
            if j not in rank:
                rank[j] = dict()
                rank[j]['weight'] = 0
            if i not in rank[j]:
                rank[j][i] = dict()
                rank[j][i]['reason'] = 0
            rank[j]['weight'] += pi * wj  # 计算用户对物品j的兴趣
            rank[j][i]['reason'] = pi * wj
    return rank  # sorted(rank.items(), key=operator.itemgetter(1), reverse=True)


def test():
    train = dict()

    train['E'] = {'b': 1, 'c': 1, 'e': 1}
    train['A'] = {'a': 1, 'b': 1, 'd': 1}
    train['B'] = {'c': 1, 'd': 1}
    train['C'] = {'b': 1, 'c': 1, 'd': 1}
    train['D'] = {'a': 1, 'd': 1}
    print("sim1", item_similarity(train))
    print("sim2", item_similarity2(train))
    print("sim3", item_similarity3(train, 0.5))
    # print(recommendation(train, 'A', item_similarity(train), 10))

test()

