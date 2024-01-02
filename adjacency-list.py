import sys;
import collections;
sys.stdin = open("input.txt", "r");
# two inputs : number of nodes , number of edges
# next n lines : u v w
'''
ADJ MATRIX
ADJ LIST
'''

'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C 
A F
C E
C F
C D
D E 
D G
G F
'''



graph  = collections.defaultdict(list);
v , e = map(int, input().split())

for i in range(e):
  u, v = input().split();
  graph[u].append(v);
  graph[v].append(u);
print("Adjacency list:");
print(graph);
for v in graph:
  print(v , graph[v])
