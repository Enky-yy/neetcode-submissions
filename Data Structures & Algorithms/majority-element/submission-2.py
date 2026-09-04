class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts =1
        n = len(nums)
        if n==1:
            return nums[0]
        max_appearance = (n+1)/2
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                cnts+=1
                if cnts>=max_appearance:
                    return nums[i]
            else:
                cnts =1
            

        return nums[0]

        