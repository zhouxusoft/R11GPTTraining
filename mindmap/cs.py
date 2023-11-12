import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的图形
G = nx.Graph()

# 添加节点，你可以添加任意类型的节点，数字，字符，甚至自定义的对象。
G.add_node(1)
G.add_node('a')
G.add_nodes_from([2, 3])

# 添加边，边是连接两个节点的线段。
G.add_edge(1, 2)
G.add_edge('a', 3)
G.add_edges_from([(1, 3), (2, 'a')])

# 画图
nx.draw(G, with_labels=True)

# 显示图形
plt.show()
