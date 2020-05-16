class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        b = False
        for i in range (0, num+1):
            if i*i == num:
                b = True
                break
            elif i*i > num:
                break
        return b
print(Solution().isPerfectSquare(int(input("Enter number\n"))))

