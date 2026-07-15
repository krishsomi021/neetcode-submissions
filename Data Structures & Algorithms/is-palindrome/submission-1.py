class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = "".join(c for c in s if c.isalnum()).lower()
        j = len(s)-1

        for i in range(len(s)//2):
            
            if(s[i] == s[j]):
                j-=1
                continue
            else:
                return False
        return True

        