class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)

        sorted_data = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        result = list(sorted_data.keys())[:k]

        return result

       





        
         
        