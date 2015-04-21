__author__ = 'Administrator'
__doc__ = '基于图的模型推荐算法'
import math


# 基于图的模型推荐
# 算法说明：
#   在图模型上，给用户u推荐物品的任务就是转换为度量用户顶点Vu和与
#   与Vu没有直接相连的物品节点在图模型上的相关性，相关性越高，则在
#   推荐列表中的权重就越高
#   度量图中两个顶点之间的相关性取决与：
#       1.两顶点之间的路径数，路径越多相关性越高
#       2.两顶点之间的距离，即路径的长度， 距离越短相关性越高
#       3.两顶点之间的路径所经过的顶点，进过的顶点的出度越小相关性越高
#   为用户u推荐时，可以从该用户对应的节点作为根节点root在图模型上进行随机游走
#   又咋偶到任一节点时，首先按照概率p决定是继续游走，还是停止并从根节点重新游走
#   若决定继续游走，则从当前节点的出度中按照均匀分布随机选择一个节点作为下个经过的节点
#   经过有限次迭代后，每个物品节点被访问的概率将会收敛到一个数，则物品节点的访问概率就
#   作为该物品在推荐列表中的权重
# 参数说明：
#   graph：用户行为的图模型，如果用户u对物品i有过行为，则在用户u与
#          物品i之间建立一条边E<u,i>
#   alpha：
#   root：当前待推荐的用户节点
def personal_rank(graph, alpha, root):
    rank = dict()
    rank = {x: 0 for x in graph.keys()}  # 获取所有用户标识
    rank[root] = 1
    for k in range(20):
        temp = {x: 0 for x in graph.keys()}
        for i, ri in graph.items():  # 获取用户i及其有过行为的物品ri
            for j, wij in ri.items():  # 获取物品及其对应的权重
                if j not in temp:  # 初始化
                    temp[j] = 0
                # 根据如下公式：
                #   当v ！= root 时 ： PR(v) = p*sum(w / out(w)) (out(w)代表节点w所指向的节点)
                #   当v = root 时：PR(v) = 1 - alpha + p*sum(w / out(w))
                temp[j] += 0.6 * rank[i] / (float(len(ri)))
                if j == root:
                    temp[j] += 1 - alpha
        rank = temp
    return rank


def test():
    train = dict()
    train['A'] = {'a': 1, 'c': 1}
    train['B'] = {'a': 1, 'b': 1, 'c': 1, 'd': 1}
    train['C'] = {'c': 1, 'd': 1}
    train['a'] = {'A': 1, 'B': 1}
    train['b'] = {'B': 1}
    train['c'] = {'A': 1, 'B': 1, 'C': 1}
    train['d'] = {'B': 1, 'C': 1}
    print(personal_rank(train, 0.6, 'A'))

test()


