class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newstr = {}

        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key not in newstr:
                newstr[key] = []
            newstr[key].append(strs[i])
        return list(newstr.values())

        
        



        