# def deletions_for_char(s, ch):
#     """Return minimum deletions if we can only delete ch, or inf if impossible."""
#     i, j = 0, len(s) - 1
#     deletions = 0
#     while i < j:
#         if s[i] == s[j]:
#             i += 1
#             j -= 1
#         elif s[i] == ch:
#             i += 1
#             deletions += 1
#         elif s[j] == ch:
#             j -= 1
#             deletions += 1
#         else:
#             return float('inf')  # impossible for this character
#     return deletions

# def check(w):
#     n = len(w)
#     # Try every unique character in w and take the minimum deletions
#     best = min((deletions_for_char(w, ch) for ch in set(w)), default=float('inf'))
#     return -1 if best == float('inf') else best

# n = int(input())
# for i in range(n):
#     d = input()
#     w = input()
#     print(check(w))

n = int(input())
for k in range(n):
    l = int(input())
    w = input()
    checked = set()
    m = l + 1
    for ch in w:
        if not ch in checked:
            checked.add(ch)
            j = l - 1
            i = 0
            count = 0
            fl = True
            while i < j:
                if w[i] != w[j]:
                    if w[i] == ch:
                        i += 1
                        count += 1
                        continue
                    elif w[j] == ch:
                        j -= 1
                        count += 1
                        continue
                    else:
                        fl = False
                        break
                i += 1
                j -= 1
            if fl:
                m = min(m, count)
    print(-1 if m == l+1 else m)




