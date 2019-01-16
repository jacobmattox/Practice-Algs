

def matrixMult(_matA, _matB):
    returnMat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(len(_matA)):
        for j in range(len(_matB[0])):
            for k in range(len(_matA)):
                returnMat[i][j] += _matA[i][k] * _matB[k][j]
    return returnMat
def main():
    matA = [[1, 0, 2, 1],
            [4, 1, 1, 0],
            [0, 1, 3, 0],
            [5, 0, 2, 1]]
    matB = [[0, 1, 0, 1], 
            [2, 1, 0, 4],
            [2, 0, 1, 1],
            [1, 3, 5, 0]]
    print(matrixMult(matA, matB))
        
main()
