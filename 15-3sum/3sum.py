class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        r=[]
        for fir in range(len(nums)):
            if fir > 0 and nums[fir] == nums[fir-1]:
                continue
            if nums[fir] > 0:
                break
            left=fir+1
            right=len(nums)-1
            while left<right:
                sum=nums[fir]+nums[left]+nums[right]

                if sum>0:
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    r.append([nums[fir],nums[left],nums[right]])
                    left+=1
                    right-=1
            
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
            
        return r
            


                


