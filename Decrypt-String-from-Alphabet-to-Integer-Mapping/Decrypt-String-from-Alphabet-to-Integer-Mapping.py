class Solution:
    def freqAlphabets(self, s: str) -> str:
        c = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                c.append(chr(int(s[i-2:i]) + 96))
                i -= 3
            else:
                c.append(chr(int(s[i]) + 96))
                i -= 1
        return ''.join(c[::-1])