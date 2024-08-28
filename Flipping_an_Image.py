class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            left, right = 0, len(image) - 1

            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                image[i][left] = 0 if image[i][left] else 1
                image[i][right] = 0 if image[i][right] else 1

                left += 1
                right -= 1
            
            if len(image) % 2:
                image[i][left] = 0 if image[i][left] else 1
        
        return image
