import re as re
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn import preprocessing
from collections import deque
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

def compare_list_dict(l1, l2):
    for item1 in l1:
        for item2 in l2:
            if (item1['v1'] == item2['v1'] and
                item1['v2'] == item2['v2'] and
                item1['weight'] == item2['weight']):
                    return True
    return False

def main():
    df = pd.read_csv('data.csv', sep = ';')

    print(df)
    print()

    nodes = []

    for w, row in df.iterrows():
        for k, value in enumerate(row):
            if value is not 'x' and value is not '-' and value is not np.nan:
                node = dict()

                node['weight'] = int(value)
                node['v1'] = w + 1
                node['v2'] = k + 1

                nodes.append(node)
 
    sorted_nodes = sorted(nodes, key = lambda item: item['weight']) 

    selected_nodes = []
    selected_v = []

    selected_nodes.append([sorted_nodes[0]])

    for index1, value1 in enumerate(sorted_nodes[1:]):
        flag1 = False
        for index2, value2 in enumerate(selected_nodes):
            flag2 = False
            compare = dict()
                
            compare[value1['v1']] = False
            compare[value1['v2']] = False

            for index3, value3 in enumerate(value2):
                if ((value1['v1'] == value3['v1'] and value1['v2'] != value3['v2']) or
                    (value1['v1'] == value3['v2'] and value1['v2'] != value3['v1'])):
                        compare[value1['v1']] = True

                if ((value1['v2'] == value3['v2'] and value1['v1'] != value3['v1']) or
                    (value1['v2'] == value3['v1'] and value1['v1'] != value3['v2'])):
                        compare[value1['v2']] = True
                        
            if ((compare[value1['v1']] == True and compare[value1['v2']] == False) or
                (compare[value1['v2']] == True and compare[value1['v1']] == False)):
                flag2 = True
            else:
                flag1 = True

            if flag2 == True:
                selected_nodes[index2].append(value1)

        if flag1 == True:
            selected_nodes.append([value1])
        else:
            temp = selected_nodes[0]
            
            for index2, value2 in enumerate(selected_nodes[1:]):
                if compare_list_dict(temp, value2):
                    for item in temp:
                        if index2 + 1 < len(selected_nodes):
                            selected_nodes[index2 + 1].append(item)
                            selected_nodes[index2 + 1] = [i for n, i in enumerate(selected_nodes[index2 + 1]) if i not in selected_nodes[index2 + 1][n + 1:]]
                    del selected_nodes[index2]

    sum = 0

    for item in selected_nodes[0]:
        sum += item['weight']
        print(item)

    print()
    print("Suma: " + str(sum))
    print()

    G1 = nx.Graph()

    for item in sorted_nodes:
        G1.add_edge(item['v1'], item['v2'], weight = item['weight']) 

    G2 = nx.Graph()

    for item in selected_nodes[0]:
        G2.add_edge(item['v1'], item['v2'], weight = item['weight']) 

    pos = nx.shell_layout(G1)
    nx.draw(G1, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G1,'weight')
    nx.draw_networkx_edge_labels(G1, pos, edge_labels = edge_labels)
    nx.draw(G2, pos, edges=G2.edges(), edge_color='r', width=5)

    plt.show()
if __name__ == "__main__":
    main()