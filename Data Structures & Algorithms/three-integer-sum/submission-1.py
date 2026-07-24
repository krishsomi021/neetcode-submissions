class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicate starting values

            begin = i + 1
            end = len(nums) - 1

            while begin < end:
                currsum = nums[i] + nums[begin] + nums[end]

                if currsum > 0:
                    end -= 1
                elif currsum < 0:
                    begin += 1
                else:
                    result.append([nums[i], nums[begin], nums[end]])
                    begin += 1
                    end -= 1
                    while begin < end and nums[begin] == nums[begin - 1]:
                        begin += 1  # skip duplicate begin values
                    while begin < end and nums[end] == nums[end + 1]:
                        end -= 1  # skip duplicate end values

        return result
    






            
        