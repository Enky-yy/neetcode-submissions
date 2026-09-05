class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_appearance = (len(nums)+1)/3
        cnts=1
        ans = []
        if len(nums) in (1,2):
            return nums
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                cnts+=1
                if cnts>= max_appearance and nums[i] not in ans:
                    ans.append(nums[i])
            else:
                cnts=1
        return ans