class Solution:
    def rotatedDigits(self, n: int) -> int:
        return sum(
            1 for i in range(1,n+1)
            if (s:= set(str(i))) & {'2','5','6','9'} and not s & {'3','4','7'}
        )