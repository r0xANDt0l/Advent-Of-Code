class Board:
    def __init__(self, size) -> None:
        self.board = [[0 for i in range(size)] for j in range(size)]

    def putLine(self, startPos , endPos):
        movX = 0 if startPos[0] == endPos[0] else 1 if startPos[0] < endPos[0] else -1
        movY = 0 if startPos[1] == endPos[1] else 1 if startPos[1] < endPos[1] else -1

        while startPos != endPos:
            self.board[startPos[0]][startPos[1]] += 1
            startPos[0] += movX
            startPos[1] += movY
        
        self.board[startPos[0]][startPos[1]] += 1

    def crossPoints(self)-> int:
        ret = 0
        for i in self.board:
            for j in i:
                if j > 1:
                    ret += 1
        return ret
    
    def print(self):
        for i in self.board:
            print(i)

def ex1(input: list[str], diagonal : bool) -> int:
    board = Board(1000)
    
    for i in input:
        positions = i.split('->')
        startPos = positions[0].split(',')
        endPos = positions[1].split(',')
        x1 = int(startPos[0])
        y1 = int(startPos[1])
        x2 = int(endPos[0])
        y2 = int(endPos[1])
        if x1 == x2 or y1 == y2 or diagonal:
            board.putLine([x1,y1],[x2,y2])

    return board.crossPoints()


file = open("Day5/data.txt")

lines = file.readlines()

print(ex1(lines, False))
print(ex1(lines, True))