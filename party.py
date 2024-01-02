import sys
sys.stdin = open("input.txt", 'r')

while True:
  n = int(input())
  if n == 0:
    break
  a = []
  for i in range(n):
    a.append(int(input()))
  a.sort()
  for i in range(n):
    print(a[i])
