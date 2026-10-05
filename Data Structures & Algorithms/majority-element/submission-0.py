class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count==0:
                n = nums[i]
        
            if nums[i]==n:
                count+=1
            else:
                count-=1

        return n
            