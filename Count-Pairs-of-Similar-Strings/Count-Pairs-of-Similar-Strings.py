class Solution:
    def similarPairs(self, words: list[str]) -> int:
        words_set = {}
        count = 0
        for w in words:
            s = frozenset(w)
            words_set[s] = words_set.get(s, 0) + 1
        for v in words_set.values():
            count += (v**2 - v)/2
        return int(count)