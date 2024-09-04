MOD = 10**9 + 7

def mex_sum(n, a):
    freq = [0] * (n + 1)
    answer = 0

    for num in a:
        freq[num] += 1

    for i in range(n):
        if freq[i] == 0:
            answer = (answer + pow(2, i, MOD)) % MOD
        else:
            freq[i] -= 1

    return answer

def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        a = list(map(int, input().split()))

        result = mex_sum(n, a)
        print(result)

if __name__ == "__main__":
    main()
