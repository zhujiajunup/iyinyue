__author__ = 'JJZhu'
import math
import random

user_tags = dict()  # 存储用户u打过标签b的次数
tag_items = dict()  # 存储物品i被打过标签b的次数
user_items = dict()  # 存储用户u打过标签的物品集合
tag_users = dict()  # 存储标记过标签i的用户集合


# 计算标签流行度
# 参数说明：
# records: 记录了<user, item, tag>三元组的标签记录
# 计算物品i, j的余弦相似度
def cosine_sim(item_tags, i, j):
    ret = 0
    for b, wib in item_tags[i].items():
        if b in item_tags[j]:
            ret += wib * item_tags[j][b]
    ni = 0
    nj = 0
    for b, w in item_tags[i].items():
        ni += w * w
    for b, w in item_tags[j].items():
        nj += w * w
    if ret == 0:
        return 0
    return ret / math.sqrt(ni * nj)


# 计算推荐列表的多样性
def diversity(item_tags, recommend_items):
    ret = 0
    n = 0
    for i in recommend_items.keys():
        for j in recommend_items.keys():
            if i == j:
                continue
            ret += cosine_sim(item_tags, i, j)
            n += 1
    return 1 - ret / float(n)


# 计算新颖性
def popularity(item_pop, recommend_items):
    ret = 0
    n = 0
    for i in recommend_items.keys():
        ret += math.log(1 + item_pop[i])
    return ret / float(len(recommend_items))


def init_stat(records):

    for user, item, tag in records:
        add_value_to_mat(user_tags, user, tag, 1)
        add_value_to_mat(tag_items, tag, item, 1)
        add_value_to_mat(user_items, user, item, 1)
        add_value_to_mat(tag_users, tag, user, 1)


# 统计辅助函数
# 对矩阵mat所对应的mat[key][value] 增加 x
def add_value_to_mat(mat, key, value, x):
    if key not in mat:
        mat[key] = dict()
    if value not in mat[key]:
        mat[key][value] = 0
    mat[key][value] += x


# 基于用户标签的推荐算法
def recommend(user):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommend_items:
                recommend_items[item] = 0
            recommend_items[item] += wut * wti
    return recommend_items


# 改进后的算法
def recommend2(user):
    recommend_items = dict()
    tagged_items = user_items[user]
    for tag, wut in user_tags[user].items():
        for item, wti in tag_items[tag].items():
            if item in tagged_items:
                continue
            if item not in recommend_items:
                recommend_items[item] = 0
            recommend_items[item] += wut / math.log(1 + len(tag_users[tag])) * wti
    return recommend_items


def test():
    r = []
    r.append(['A', 'a', '1'])
    r.append(['B', 'b', '2'])
    r.append(['C', 'c', '1'])
    r.append(['C', 'b', '2'])
    r.append(['B', 'a', '2'])
    r.append(['D', 'b', '1'])
    r.append(['E', 'b', '2'])
    r.append(['E', 'c', '1'])
    init_stat(r)
    print(tag_users)
    print(tag_items)
    print(user_items)
    print(user_tags)
    print(recommend('A'))
    print(recommend2('A'))


# 读取测试文件
def read_file():
    re = []
    data_file = open('DeliciousDataset.txt', 'r', encoding='utf-8')
    done = 0
    count = 0
    while not done:
        randint = random.randint(0, 500)
        print(randint)
        if randint < 495:
            continue
        line = data_file.readline()
        if line != '':
            line = line.strip()
            record = line.split("\t")
            if len(record) <= 2:
                continue
            tags = record[2]
            for tag in tags.split(" "):
                re.append([record[0], record[1], tag])
                print([record[0], record[1], tag])
                count += 1
        else:
            done = 1
    print("total count", count)
    return re


r = read_file()
init_stat(r)
print("recommend for user: 226777:\n", recommend('226777'))
print("recommend2 for user: 226777:\n", recommend2('226777'))