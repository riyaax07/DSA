class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix={0:1}
        sum=0
        count=0
        for ch in nums:
            sum+=ch
            rem=sum-k
            if rem in prefix:
                count+=prefix[rem]
            prefix[sum]=prefix.get(sum,0)+1
        return count


        