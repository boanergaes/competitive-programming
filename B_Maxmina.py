n = int(input())
for i in range(n):
    [m, k] = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for z in arr:
        if z == 1:
            print('YES')
            break
    else:
        print('NO')