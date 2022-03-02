#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts UNWEIGHTED_INTEGER_GRAPH tree as parameter.
#

#
# For the unweighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].
#
# 트리가 주어진다. 트리의 지름의 양 끝점이 될 수 있는 노드들을 구하시오.
#
from collections import deque

def get_furthest_node(A, edges, n):
    queue = deque()
    is_visited = [False]*(n+1)
    queue.append(A)
    while queue:
        cur = queue.popleft()
        if is_visited[cur]:
            continue
        is_visited[cur] = True
        for next_node in edges[cur]:
            if not is_visited[next_node]:
                queue.append(next_node)
    return cur


def get_furthest_node_and_route(A, edges, n):
    queue = deque()
    is_visited = [False]*(n+1)
    queue.append((A, 0))
    dist = [0]*(n+1)
    while queue:
        cur, count = queue.popleft()
        if is_visited[cur]:
            continue
        is_visited[cur] = True
        dist[cur] = count
        for next_node in edges[cur]:
            if not is_visited[next_node]:
                queue.append((next_node, count+1))
    X = cur
    i = count
    route = []
    while i >= 0:
        for next_node in edges[cur]:
            if dist[next_node] == i-1:
                break
        route.append(cur)
        cur = next_node
        i -= 1
        
    return X, count, route


def get_special_nodes(A, edges, n, route, d):
    specials = []
    queue = deque()
    is_visited = [False]*(n+1)
    queue.append((A, 0, 0))
    in_route = [False]*(n+1)
    for node in route:
        in_route[node] = True
    while queue:
        cur, count, out = queue.popleft()
        if (count == d) or (out*2 == count):
            specials.append(cur)
        if is_visited[cur]:
            continue
        is_visited[cur] = True
        for next_node in edges[cur]:
            if not is_visited[next_node]:
                new_out = out
                if not in_route[next_node]:
                    new_out += 1
                queue.append((next_node, count+1, new_out))
    return specials

def solution(tree_nodes, tree_from, tree_to):
    edges = dict()
    n = tree_nodes
    answer = [0]*n
    specials = []
    for i in range(1, n+1):
        edges[i] = []
    for i in range(n - 1):
        edges[tree_from[i]].append(tree_to[i])
        edges[tree_to[i]].append(tree_from[i])
    X = get_furthest_node(1, edges, n)
    Y, d, route = get_furthest_node_and_route(X, edges, n)
    specials = get_special_nodes(route[0], edges, n, route, d)
    for special in specials:
        answer[special-1] = 1
    return answer


'''
후기

'''