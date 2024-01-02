import sys
sys.stdin = open("input.txt", 'r')
for _ in range(int(input())):
  c = False
  n = int(input())
  if n < 2020:
    print("NO")
    continue
  elif n% 2020 ==0 :
    print("YES")
    continue
  elif n% 2021 ==0 :
    print("YES")
    continue
  else:
    while n >0:
      n-=2021
      if n%2020 == 0 and n >0:
        print("YES")
        c = True
        break
  if not c:
    print("NO")
