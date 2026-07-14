class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        newnums = set(nums)
        maxconsec = 0

        for n in nums:
            if n-1 not in newnums:
                length = 0

                while n+length in newnums:
                    length+=1
                maxconsec = max(length, maxconsec)

        return maxconsec

            
        
                



            



        