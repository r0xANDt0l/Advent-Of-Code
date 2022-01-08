from os import remove


class Board:
    def __init__(self, board: list[str]) -> None:
        self.board = [[j for j in i.split(" ") if j != ""] for i in board]

    def checkNumber(self, number: str) -> bool:
        for i in range(5):
            for j in range(5):
                check = self.board[i][j]
                if  check == number or number + '\n' == check:
                    self.board[i][j] = 'x'
                    return self.checkWin((i, j))

        return False

    def checkWin(self, pos: tuple()) -> bool:
        return self.checkLine(pos[0]) or self.checkColumn(pos[1])

    def checkLine(self, line) -> bool:
        ret = True
        for i in range(5):
            ret *= self.board[line][i] == 'x'
        return ret

    def checkColumn(self, column) -> bool:
        ret = True
        for i in range(5):
            ret *= self.board[i][column] == 'x'
        return ret
           
       
    def score(self) -> int:
        ret = 0
        for i in range(5):
            for j in range(5):
                ret += int(self.board[i][j]) if self.board[i][j] != 'x' else 0
        return ret
   
    def print(self):
        for i in self.board:
            print(i)


def ex1(input: list[str]) -> int:
    numbers = input[0].split(",")
    boards = []

    for i in range(int((len(input) - 1) / 5)):
        boards.append(Board(input[(i * 5) + 1 : (i * 5) + 6]))

    for i in numbers:
        for j in boards: 
            if j.checkNumber(i):
                return j.score() * int(i)

def ex2(input : list[str]) -> int:
    numbers = input[0].split(",")
    boards = []

    for i in range(int((len(input) - 1) / 5)):
        boards.append(Board(input[(i * 5) + 1 : (i * 5) + 6]))

    for i in numbers:
        toRemove = []
        for j in boards:
            if j.checkNumber(i):
                if len(boards) == 1:
                    return j.score() * int(i)
                toRemove.append(j)
        for j in toRemove:
            boards.remove(j)


file = open("Day4/data.txt")

lines = file.readlines()

lines = [i for i in lines if i != "\n"]

print(ex1(lines))
print(ex2(lines))
