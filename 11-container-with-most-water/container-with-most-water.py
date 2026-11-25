class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            con=(right-left)*(min(height[left],height[right]))
            max_area=max(con,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return(max_area)
            

        