class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n= len(fruits)
        i,j= 0,0
        max_length=0
        count= {}
        #k=2
        while j<n:
            count[fruits[j]]= count.get(fruits[j],0)+1
            if len(count)<=2:
                max_length= max(max_length,j-i+1)
                j+=1
            elif len(count)>2:
                while len(count)>2:
                    count[fruits[i]]-=1
                    if count[fruits[i]]==0:
                        del count[fruits[i]]
                    i+=1
                j+=1
        return max_length