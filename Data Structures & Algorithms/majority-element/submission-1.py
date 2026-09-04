class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_cnts=1
        cnts =1
        ans =0
        if len(nums)==1:
            return nums[0]
        max_appearance = (len(nums)+1)/2
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                cnts+=1
                max_cnts = max(cnts, max_cnts)
            else:
                cnts =1
            if max_cnts>=max_appearance:
                ans=i
                break

        return nums[ans]

        