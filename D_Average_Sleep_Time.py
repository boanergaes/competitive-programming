ia = input().split()

n = int(ia[0])
k = int(ia[1])

inp = [int(i) for i in input().split()]

s = sum(inp[:k])
t = s
for i in range(k, n):
    t -= inp[i - k]
    t += inp[i]
    s += t
print(f"{s/(n-k+1):.10f}")