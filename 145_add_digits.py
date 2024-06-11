class Solution:
    def addDigits(self, num: int) -> int:
        def sums(num):
            return sum(int(digits) for digits in str(num))

        while num >= 10:
            num = sums(num)

        return num