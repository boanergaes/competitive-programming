class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = x
        n = 0
        while r > 0:
            n = 10 * n + r % 10 
            r //= 10
        return x == n