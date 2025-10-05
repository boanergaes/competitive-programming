#================ DOESN'T WORK YET =====================

[n, m] = map(int, input().split())
wrld_map = list(map(int, input().split()))
toright, toleft = [0], [0]
for i in range(1, n):
    dmg = wrld_map[i-1] - wrld_map[i] if wrld_map[i] < wrld_map[i-1] else 0
    toright.append(toright[-1] + dmg)
for i in range(n - 1, 1, -1):
    dmg = wrld_map[i] - wrld_map[i-1] if wrld_map[i] > wrld_map[i-1] else 0
    toleft.append(toright[-1] + dmg)
toleft.reverse()
for i in range(m):
    [s, t] = list(map(int, input().split()))
    s -= 1
    t -= 1
    if s < t:
        print(toright[t] - toright[s])
    else:
        print(toleft[t] - toleft[s])

