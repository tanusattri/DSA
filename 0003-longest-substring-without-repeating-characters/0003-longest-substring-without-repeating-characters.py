class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n= len(s)
        i,j= 0,0
        max_length=0
        count= {}
        while j<n:
            count[s[j]]= count.get(s[j],0)+1
            if len(count)== (j-i+1):
                max_length= max(max_length, j-i+1)
                j+=1
            elif len(count)< (j-i+1):
                while len(count)<(j-i+1):
                    count[s[i]]-=1
                    if count[s[i]]==0:
                        del count[s[i]]
                    i+=1
                j+=1
        return max_length