class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board: #row check
            hold = []
            for v in row:
                if v not in hold:
                    hold.append(v)
                elif v != ".":
                    return False
        for col in range(len(board)): #col check
            hold = []
            for row in range(len(board)):
                if board[row][col] not in hold:
                    hold.append(board[row][col])
                elif board[row][col] != ".":
                    return False
        for i in range(3):  #box check
            
            for j in range(3):
                hold = []
                for k in range(3):
                    for f in range(3):
                        if board[3*i+k][3*j+f] not in hold:
                            hold.append(board[3*i+k][3*j+f])
                        elif board[3*i+k][3*j+f] != ".":
                            return False
        return True