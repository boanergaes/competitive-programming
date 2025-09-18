class Solution:
    def longestCommonPrefix(self, strs):
        ref = list(strs[0])
        for w in strs[1:]:
            if len(ref) > len(w):
                ref = ref[:len(w)]
            for j in range(len(ref) - 1, -1, -1):
                if ref[j] != w[j]:
                    n = len(ref)
                    for k in range(n-1, j-1, -1):
                        ref.pop(k)
        return ''.join(ref)