
import sys
sys.stdin = open("inn.txt", "r");

while True:
  n = int(input())
  if n == 0:
    break;
  a = list(map(int, input().split()))
  b = [0]*n
  b[0] = a[0]
  for i in range(1, n):
    b[i] = a[i] + b[i-1]

  while True:
     x , y = map(int, input().split())
     if x == 0 and y == 0:
       break;
     print(b[y] - b[x-1]);
  

  

