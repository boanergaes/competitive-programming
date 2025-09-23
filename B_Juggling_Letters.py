n = int(input())
for inp in range(n):
    r = int(input())
    char_count = {}
    for i in range(r):
        w = input()
        for c in w:
            char_count[c] = char_count.get(c, 0) + 1
    for v in char_count.values():
        if v % r != 0:
            print('NO')
            fl = False
            break
    else:
        print('YES')



