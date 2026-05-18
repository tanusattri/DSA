class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n= len(arr)
        vis= [False]*n
        m= defaultdict(list)
        for i in range(n):
            m[arr[i]].append(i)
        q= deque()
        s= set()
        q.append(0)
        jump=0
        vis[0]= True
        while q:
            size= len(q)
            while size>0:
                size-=1
                curr= q.popleft()
                if curr==n-1:
                    return jump
                if curr+1<n and not vis[curr+1]:
                    q.append(curr+1)
                    vis[curr+1]= True
                if curr-1>=0 and not vis[curr-1]:
                    q.append(curr-1)
                    vis[curr-1]=True
                if arr[curr] in s:
                    continue
                for idx in m[arr[curr]]:
                    if not vis[idx]:
                        q.append(idx)
                        vis[idx]= True
                s.add(arr[curr])
            jump+=1
        return jump