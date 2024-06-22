class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        l = r = ans = 0
        for c in s:
            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            if l == r:
                ans += 1
                l = r = 0 #RESETTING AGAIN THE COUNTER TO FIND NEXT SUBSTRING
        return ans
    
    
