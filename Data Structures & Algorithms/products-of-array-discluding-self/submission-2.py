class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product =1
        num_check=0
        for num in nums:
            if(num==0):
                num_check+=1
            else:
                product*=num

        n = len(nums)
        if (num_check==0):
            for i in range(n):
                nums[i] = int(product/nums[i])
        elif(num_check>1):
            for i in range(n):
                nums[i]=0
        else:
            for i in range(n):
                if(nums[i]==0):
                    nums[i]= product *(num_check)
                else:
                    nums[i]=0
        return nums