class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        i = -1

        for gola in range(len(nums)-1, 0, -1):
            if nums[gola-1] < nums[gola]:
                i = gola-1
                break

        if i >= 0:
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        left, right = i + 1, len(nums)-1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1