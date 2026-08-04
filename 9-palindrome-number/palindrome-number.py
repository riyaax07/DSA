class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        pal=x
        while(pal>0):
            dig=pal%10
            rev=rev*10+dig
            pal=pal//10
        if rev==x:
            return True
        else:
            return False
        