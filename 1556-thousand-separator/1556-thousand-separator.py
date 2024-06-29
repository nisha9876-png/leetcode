class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
        
        result = ""
        count = 0
        while n > 0:
            if count > 0 and count % 3 == 0:
                result = "." + result
            result = str(n % 10) + result
            n //= 10
            count += 1
        
        return result

    
    
    
   
            