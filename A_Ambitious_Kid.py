n = int(input())
inp = list(map(int, input().split()))
min_elem = float('inf')
for i in inp:
    if i == 0:
        print(0)
        break
    min_elem = min(min_elem, abs(i))
else:
    print(min_elem)