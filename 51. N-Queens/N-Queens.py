class Solution:
    def __init__(self) -> None:
        self.boardSize = 0       # 棋盤大小
        self.result = []         # 輸出的答案組合
        self.queen = []      # 目前 Queen 的所在位置
        self.cols = []

    def checkAvailable(self, coor: tuple) -> bool:
        row = coor[0]
        col = coor[1]

        # 檢查是同個 col 中是否有 Queen
        if col in self.cols:
            print('checkAvailable FALSE, coor = %s, cols = %s' %(coor, self.cols))
            return False
        
        # 算出左斜角的所有位置
        checkTargetDia = list()
        for i in range(1, row + 1):
            checkTargetDia.append((row - 1 * i, col - 1 * i))

        # 算出右斜角的所有位置
        checkTargetOffDia = list()
        for i in range(1, row + 1):
            checkTargetOffDia.append((row - 1 * i, col + 1 * i))

        checkTarget = list()
        checkTarget = checkTargetDia + checkTargetOffDia

        # 檢查是斜角中是否有 Queen
        for item in self.queen:
            if item in checkTarget:
                print('checkAvailable FALSE, coor = %s, cols = %s, checkTarget = %s' %(self.cols, coor, checkTarget))
                return False

        print('checkAvailable FALSE, coor = %s, cols = %s, checkTarget = %s' %(coor, self.cols, checkTarget))
        return True

    def resultFormat(self) -> list[str]:
        print('resultFormat queen = %s' %(self.queen))
        board = list()
        for item in self.queen:
            formatString = "." * item[1] + "Q" + "." * (self.boardSize - item[1] - 1)
            print('resultFormat formatString = ' + str(formatString))
            board.append(formatString)
        
        print('resultFormat board = %s' + str(board))
        return board

    def dfs(self, row: int):
        if row == self.boardSize:
            print('dfs find solution!')
            self.result.append(self.resultFormat())
        else:
            print('dfs tracing')
            for col_idx in range(self.boardSize):
                currentCoor = (row, col_idx)
                print('dfs currentCoor = ' + str(currentCoor))
                if self.checkAvailable(currentCoor):
                    self.queen.append(currentCoor)
                    self.cols.append(col_idx)

                    self.dfs(row + 1)

                    self.queen.remove(currentCoor)
                    self.cols.remove(col_idx)

    def solveNQueens(self, n: int) -> list[list[str]]:
        self.boardSize = n
        self.dfs(0)
        return self.result


eightQueens = Solution()
print(eightQueens.solveNQueens(4))