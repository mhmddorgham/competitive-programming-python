import sys
sys.stdin = open("input.txt", 'r')
def get_pos(hops, i, s):
   while hops:
      if int(s[i]) %2 == 0:
        i+=int(s[i])
      else:
        i-=int(s[i])

      i = i%len(s)
  
      hops-=1
   return i+1

for _ in range(int(input())):
  hops, i, s= input().split()
  hops = int(hops)
  i = int(i) -1

  print(get_pos(hops, i, s))
  
 



