class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x <0  :
            return False
        if x == 0:
            return True
        elif x%10==0 :
            return False
        rev = 0
        while x > rev:
            rem = x%10
            rev = rev*10+rem
            x = int(x/10)
        return x==rev or x==int(rev/10)