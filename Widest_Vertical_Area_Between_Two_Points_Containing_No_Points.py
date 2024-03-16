class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(point[0] for point in points)

        return (max((points[i+1]-points[i] for i in range(len(points)-1))))
