import sys

sys.stdin = open("input.txt", "r")

import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if(math.gcd(*a) == math.gcd(*b)):
        print(0);
    elif(math.gcd(*a) % math.gcd(*b) ==0 or math.gcd(*b) % math.gcd(*a) ==0 ):
        print(1)
    else:
        print(2)
