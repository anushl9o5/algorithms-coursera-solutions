from random import choice
from copy import deepcopy

def random_select_edge(graph):
    v1 = choice(list(graph.keys()))
    v2 = choice(list(graph[v1]))

    return (v1, v2)


def min_cut(adj_list):

    while len(adj_list) > 2:
        
        node1, node2 = random_select_edge(adj_list)        

        adj_list[node1].extend(adj_list[node2])
        
        for vertex in adj_list[node2]:
            adj_list[vertex].remove(node2)
            adj_list[vertex].append(node1)

        while node1 in adj_list[node1]:
            adj_list[node1].remove(node1)

        adj_list.pop(node2)
        
    count = 0
    for key in adj_list:
        count+=(len(adj_list[key])//2)
        
    return count

if __name__ == "__main__":
    adj_list = {}
    with open('adjacency_list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            adj_ele = line.split("\t")[:-1]
            adj_list[adj_ele[0]] = adj_ele[1:]
    
    total_count = []
    for i in range(1600): #nlogn iterations => P[Fail] = 1/n
        total_count.append(min_cut(deepcopy(adj_list)))

    print(min(total_count))
