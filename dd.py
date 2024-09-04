import math
import sys

sys.stdin = open("input.txt", "r")
t = int(input())
while t:
    a,percent = input().split()
    a = int(a)
    percent = int(percent)
    
    b = 1
    flag = False
 
    while True:
        if percent == 100:
            flag = True
            break
 
        temp = 0
        temp = (percent/100) * (a+b)
 
 
        if b >= temp:
            break
        b += 1
 
    if flag:
        print(-1)
    else:
        print(a+b)
        
    t -= 1