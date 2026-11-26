class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove =10
        ali=True
        while n>=remove:
            n=n-remove
            remove-=1
            ali= not ali
        if not ali:
            return True
        else:
            return False

            



        