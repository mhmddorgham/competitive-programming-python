import math
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
