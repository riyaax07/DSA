class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for j in range(len(nums)):
            swapped=False
            for i in range(0,len(nums)-j-1):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    swapped=True
            if not swapped:
                break
        return nums

        """
        Do not return anything, modify nums in-place instead.
        """
        