class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_volume = 0
        while l < r:
            min_height = min(heights[l], heights[r])
            volume = min_height * (r - l)
            max_volume = max(max_volume, volume)
            if heights[l] <= heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
        return max_volume