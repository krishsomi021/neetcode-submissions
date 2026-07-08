class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums)) # initialize result array with 1's as all the values for each index

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] 
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

            

        