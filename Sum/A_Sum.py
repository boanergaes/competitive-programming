n = int(input())
for _ in range(n):
    inp = input()
    inp = inp.split()
    i = int(inp[0])
    j = int(inp[1])
    k = int(inp[2])
    if i == j + k or j == i + k or k == i + j:
        print('YES')
    else:
        print('NO')