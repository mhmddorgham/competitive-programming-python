import sys

sys.stdin = open("input.txt", "r")

for _ in range(int(input())):
  x, y = map(int, input().split());
  if x == 0 or y == 0 or y == 100:
    print(-1)
    continue
  a = x;
  b = 1;
  temp = float(y/100) * (a+b);

  while b < temp:
    b += 1;
    temp = float(y/100) * (a+b);
  print(a+b)

  
     