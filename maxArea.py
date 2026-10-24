class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        rig=len(height)-1
        maxaa=0
        
        while left<rig :
            area=min(height[left], height[rig])*(rig-left)
            if area>maxaa:
                maxaa=area
            if height[left] < height[rig]:
                left += 1
            else:
                rig -= 1
        return maxaa
