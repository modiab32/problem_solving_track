class Solution:
    def largestRectangleArea(self, heights):
        mono = []
        max_area = 0
        for i,h in enumerate(heights):
            start= i
            while mono and mono[-1][1] > h:
                index , height = mono.pop()
                max_area = max(max_area , (i-index)*height)
                start = index
            mono.append((start,h))
            
        for i, h in mono:
            max_area = max(max_area , h*(len(heights) - i))
        return max_area
