'''
"Eternal Truths." Problem 
In this problem, you are given a graph and a series of queries where each query consists of a starting node and a Time To Live (TTL). 
The goal is to find the number of nodes that cannot be reached from the given starting node within the specified TTL.
'''
import collections
import sys
sys.stdin = open("input.txt", "r");

cases = 0
while True:  
    n = int(input())
    if n == 0:
        break
    graph = collections.defaultdict(list)

    for i in range(n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    while True:
        s, d = map(int, input().split())
        if s == 0 and d == 0:
            break;
        cases += 1
        visited = set()
        queue = collections.deque()
        queue.append((s, 0))  
        visited.add(s)

        while queue:
            u, ttl = queue.popleft()
            for v in graph[u]:
                if v not in visited and ttl < d:
                    queue.append((v, ttl + 1))
                    visited.add(v)

        unreachable_nodes = len(graph) - len(visited) 
        print(f"Case {cases}: {unreachable_nodes} nodes not reachable from node {s} with TTL = {d}.")
