from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        count = [Counter(w) for w in words]
        res = []
        for rk in count[0]:
            min_app = count[0][rk]
            for i in range(1, len(count)):
                min_app = min(min_app, count[i].get(rk, 0))
            res.extend([rk]*min_app)
        return res