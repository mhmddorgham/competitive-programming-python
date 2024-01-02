# bitwise operator and - &
# bitwise operator or - |
# bitwise operator not - ~
# bitwise operator xor - ^
# bitwise operator  right shift - >> 
# bitwise operator left shift <<
# rightshift is divide in power of 2
# leftshift is multiply in power of 2

def even_odd(n):
    if n & 1 == 1:
        print("odd")
    else:
        print("even")

def mul_pow_2(x,y):
    return x << y

def div_pow_2(x,y):
    return x >> y

t = int(input())
while t:
    x,y = map(int,input().split())
    #evenodd(n)
    print(mul_pow_2(x,y))
    print(div_pow_2(x,y))
    t=t-1