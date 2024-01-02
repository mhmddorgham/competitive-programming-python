import sys;
import math
sys.stdin = open("input.txt", "r");

# 1. Sum of numbers up to n:
def sum_to_n(n):
  return n*(n+1) // 2;

s = int(input())
print(f"Sum of numbers up to {s} is {sum_to_n(s)}")

# 2. find GCD and LCM of two numbers: 
def gcd(a, b):
  if b == 0:
    return a;
  else:
    return gcd(b, a%b);


# lcm = product // gcd
def lcm(a,b):
  return a*b // gcd(a,b);

a, b = map(int, input().split());

print(f"GCD of {a}, {b} is {gcd(a,b)}, and LCM is {lcm(a,b)}");

# 3. Find Divisors of a number: 
def get_divisors(n):
  a = set();
  for i in range(1, int(math.sqrt(n)) +1):
    if n % i ==0:
      a.add(i);
      a.add(n // i);
  return list(a);

# print(math.sqrt(24));
# add star so output is numbers only without any bracket notations at the end of the beginning
print(*sorted(get_divisors(70)));

# 4. Check if n is Prime number or not :

def is_prime(n):
  if n<=1:
    return False;
  elif n == 2:
    return True;
  elif n % 2 == 0:
    return False;
  else:
    for i in range(3, int(math.sqrt(n)) + 1, 2):
      if n % i ==0:
        return False;
    return True;
    


arr = list(map(int, input().split()));
for i in range(len(arr)):
  print(is_prime(arr[i]), end=" ");


# 5. Generate prime numbers up to N:
def generate_primes(n):
  primes = [];
  for i in range(0, n+1):
    if is_prime(i):
      primes.append(i);
  return primes;

print(*generate_primes(53));


# bitwise: 
# leftshift << multiply by power of 2
# rightshift >> divide by power of 2
# and - &
# or - |
# not - ~
# xor - ^
# right shift - >>



