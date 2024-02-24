class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        output = [[0] * len(img[0]) for _ in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                total = 0
                count = 0

                for ai in [-1, 0, 1]:
                    for aj in [-1, 0, 1]:
                        bi, bj = ai + i, aj + j

                        if 0 <= bi < len(img) and 0 <= bj < len(img[0]):
                            total += img[bi][bj]
                            count += 1
                
                output[i][j] = total // count
        
        return output
