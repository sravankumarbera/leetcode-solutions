class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        n = -1
        new = ""
        while((i<len(word1))and(j<len(word2))):
            new = new + word1[i]
            n = n+1
            i = i+1
            new = new+ word2[j]
            n = n+1
            j = j+1
        if(i<len(word1)):
            while(i<len(word1)):
                new = new + word1[i]
                n = n+1
                i = i+1
        elif(j<len(word2)):
            while(j<len(word2)):
                new = new+word2[j]
                n = n+1
                j = j+1
        return new
        
