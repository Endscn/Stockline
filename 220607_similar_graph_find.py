# 두 그래프를 비교하는 방법 유사도 찾아내기

import networkx as nx

g1 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])
print(g1)
g2 = nx.complete_graph(["n{}".format(i) for i in range(0, 5)])
print(g2)

print(["n{}".format(i) for i in range(0, 5)])

x_axis = [1,2,3,4,5]
y_axis = [1,5,4,3,2]
g1 = nx.complete_graph(x_axis)
g2 = nx.complete_graph(y_axis)
plt.plot(g1)
plt.plot(g2)
plt.show

print(nx.similarity.graph_edit_distance(g1, g2))

colorpod = ['blue','green','black']
for i in range(0, 3):
    r_n = np.random.choice(g2.nodes())
    print("node removed: {}".format(r_n))
    print("edge removed: {}".format([e for e in g2.edges() if r_n in e]))
    print("몇번째인가?",r_n)
    g2.remove_node(r_n)
    plt.plot(g1,color='red')
    plt.plot(g2,color=colorpod[i])
    plt.show()
    print(nx.similarity.graph_edit_distance(g1, g2))
    print("="*50)

range_dataFrame2 = range_dataFrame[0].to_numpy()


print(range_plot)
print(range_dataFrame2)
g1 = nx.complete_graph(range_plot)
g2 = nx.complete_graph(range_dataFrame2)
plt.plot(g1)
plt.plot(g2)
plt.show()

print(nx.similarity.graph_edit_distance(g1,g2))
print("hi")







import matplotlib.pyplot as plt
import networkx as nx
G1=nx.Graph()
G1.add_node(1,pos=(1,1))
G1.add_node(2,pos=(2,2))
G1.add_node(3,pos=(3,1))
G1.add_node(4,pos=(1,5))
G1.add_edge(1,2)
G1.add_edge(1,3)
G1.add_edge(1,4)


pos=nx.get_node_attributes(G1,'pos')
plt.figure('graph1')
nx.draw(G1,pos, with_labels=True)


G2=nx.Graph()
G2.add_node(1,pos=(10,10))
G2.add_node(2,pos=(20,20))
G2.add_node(3,pos=(30,10))
G2.add_node(4,pos=(40,30))
G2.add_edge(1,2)
G2.add_edge(1,3)
G2.add_edge(1,4)
pos2=nx.get_node_attributes(G2,'pos')
plt.figure('b')
nx.draw(G2,pos2, with_labels=True)




dist = nx.graph_edit_distance(G1, G2)
print(dist)


plt.show()




















# 데이터 유사도를 통한 평점 비슷한 사람 찾아내기

ratings={
     'Dave':{'달콤한인생':5,'범죄도시':3,'샤인':3},
     'David':{'달콤한인생':5,'범죄도시':1,'샤인':4},
     'Alex':{'달콤한인생':0,'범죄도시':4,'샤인':5},
     'Andy':{'달콤한인생':2,'범죄도시':1,'샤인':5}
}
def sim_msd(data, name1, name2):
    sum = 0
    count = 0
    for movies in data[name1]:
        if movies in data[name2]: #같은 영화를 봤다면
            sum += pow(data[name1][movies]- data[name2][movies], 2)
            count += 1

    return 1 / ( 1 + (sum / count) )

sim_msd(ratings, 'Dave','Alex')
