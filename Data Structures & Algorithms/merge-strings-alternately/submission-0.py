class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i , j =0,0
        n, m = len(word1), len(word2)
        s=''
        while(i<n and j <m):
            s+=word1[i]
            s+=word2[j]
            i, j = i+1, j+1
        
        while(i<n):
            s+=word1[i]
            i+=1
        
        while(j<m):
            s+=word2[j]
            j+=1

        return s
        