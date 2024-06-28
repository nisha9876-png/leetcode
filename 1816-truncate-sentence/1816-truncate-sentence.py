class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")   # split the string using a separator 
        return " ".join(words[:k]) # join the words take first k characters by [:k]
        
        
        
        
        
        
        
        
        
        
        
       