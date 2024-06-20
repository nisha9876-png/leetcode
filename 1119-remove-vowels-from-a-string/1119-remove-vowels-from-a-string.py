class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
    
        
        letter_list = []
        
        vowel_dict = {vowels: True for vowels in 'aeiou'} #A dictionary is created to store the vowels. The keys are the vowels themselves, and the values are all True. This dictionary is used to quickly check if a character is a vowel or not.
        
        for letter in s:
            if letter.lower() not in vowel_dict:
                letter_list.append(letter)
                
        return ''.join(letter_list)

            
        