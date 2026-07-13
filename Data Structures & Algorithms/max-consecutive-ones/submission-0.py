class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final = 0 

        for i in range(len(nums)):
            if nums[i]==0:
                final = max(final, count)
                count = 0
            else:
                count += 1 

            

                
        return max(count, final)
