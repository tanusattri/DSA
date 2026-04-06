class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples= sum(apple)
        capacity.sort(reverse=True)
        boxes_used= 0
        curr=0
        for c in capacity:
            curr+= c
            boxes_used+=1
            if curr>=total_apples:
                break
        return boxes_used