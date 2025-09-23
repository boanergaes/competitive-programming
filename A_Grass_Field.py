n = int(input())

for i in range(n):
    u = input()
    u = u.split()
    l = input()
    l = l.split()

    arr = u + l

    if all(x == '0' for x in arr):
        print(0)
    elif all(x == '1' for x in arr):
        print(2)
    else:
        print(1)