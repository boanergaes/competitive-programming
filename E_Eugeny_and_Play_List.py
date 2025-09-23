p = input().split()

n = int(p[0])
m = int(p[1])

p_sum = []

for i in range(n):
    pp = input().split()
    if i == 0:
        p_sum.append(int(int(pp[0]) * int(pp[1])))
    else:
        p_sum.append(p_sum[-1] + int(pp[0]) * int(pp[1]))

arr = input().split()
i = 0
for num in arr:
    num = int(num)
    while num > p_sum[i]:
        i += 1
    print(i + 1)
