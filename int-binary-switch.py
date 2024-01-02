# n convert int into binary
def int_to_bin(n):
    return str(bin(n))[2:]

# bin to int 
def bin_to_int(s):
    return int(s,2)

# kth bit set from right
def kth_bit(n,k):
    print(str(bin(n))[2:])
    if n & (1 << (k-1)):
        print("SET")
    else:
        print("NOT SET")

# [5,3,2,3,2,1,5]
# every number occurs twice
# we need to find the number which occurs only once
# n^n = 0
# n^0 = n
def find_single_occur(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res = res ^ arr[i]
    return res


t = int(input())
while t:
    arr = list(map(int,input().split()))
    #binstring = intToBin(n)
    #integer = binToInt(binstring)
    #print(n,binstring,integer,n==integer)
    #kthbit(n,k)
    print(find_single_occur(arr))
    t=t-1