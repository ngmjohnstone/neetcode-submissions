class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            h = min(heights[l], heights[r])
            w = r - l
            a = h * w
            if a > area:
                area = a
            
            if heights[l+1] >= heights[l]:
                l += 1
            else:
                r -= 1

        return area 