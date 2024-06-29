class Solution:
    def numWays(self, s: str) -> int:
        ones = s.count("1")
        n = len(s)
        mod = 10 ** 9 + 7
        
        # Count the number of ones in the string
        ones = s.count('1')
        
        # If the number of ones is not divisible by 3, there is no valid split
        if ones % 3 != 0:
            return 0
        
        # If there are no ones, there are 3 valid splits
        if ones == 0:
            return (n - 1) * (n - 2) // 2 % mod
        
        gap1 = 0
        gap2 = 0
        curr_ones = 0
        
        for c in s:
            if c == '1':
                curr_ones += 1
            
            if c == '0':
                if curr_ones == ones // 3:
                    gap1 += 1
                if curr_ones == 2 * ones//3:
                    gap2 += 1
        return(gap1 + 1) * (gap2 + 1) % mod
        
       