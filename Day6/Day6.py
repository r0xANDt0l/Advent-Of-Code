class Lanterfish():
    def __init__(self, timer) -> None:
        self.timer = timer
    
    def newDay(self) -> bool:
        self.timer -= 1
        if self.timer == -1:
            self.timer = 6
            return True
        return False

    def print(self):
        print(self.timer)


def ex1(input: list[str], days) -> int:
    initialFish = input[0].split(',')
    
    lanternFishList = []

    for i in initialFish:
        lanternFishList.append(Lanterfish(int(i)))

    for i in range(days):
        newLanterFish = 0
        for j in lanternFishList:
            if j.newDay():
                newLanterFish += 1

        for j in range(newLanterFish):
            lanternFishList.append(Lanterfish(8))

    return len(lanternFishList)



file = open("Day6/data.txt")

lines = file.readlines()

print(ex1(lines, 80))
print(ex1(lines, 256))