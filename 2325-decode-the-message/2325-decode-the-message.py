class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        b=[]
        print(b)
        
        for i in key:
            if i!=" " and i not in b:
                b.append(i)
        result=""
        for i in message:
            if i!= " ":
                result+= chr(b.index(i)+97)
            else:
                result+=" "
        return result
        