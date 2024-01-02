
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