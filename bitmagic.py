# ispowerof 2
# n -> input
# True/False -> output
# check if n is a powerof 2
# 512 -> True 512 = 2**9
# 1024 -> True 1024 = 2**10

def is_powerof_2(n):
    # T.C = O(1)
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y

# return's number of 1's in binary representation of int
# 5 -> 101 ans = 2
# 7 -> 111 ans = 3

def brute_force_cnt_bits(n):
    # T.C = O(n)
    s = str(bin(n))[2:]
    print("{}".format(s))
    return s.count('1')


def cnt_bits(n):
    # T.C = O(logn)
    cnt = 0
    while n:
        cnt+=1
        n = n & (n-1)
    return cnt



t= int(input())
while t:
    n = int(input())
    #print(is_powerof_2(n))
    print(brute_force_cnt_bits(n))
    print(cnt_bits(n))
    t=t-1