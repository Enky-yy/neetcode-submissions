class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(2):
            for num in nums:
                l.append(num)
        return l