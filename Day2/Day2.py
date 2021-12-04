def ex1(input : list[str]) -> int:
    posX = 0
    depth = 0
    for i in range(len(lines)):
        currentLine = lines[i].split(" ")
        if str(currentLine[0]) == "forward":
            posX += int(currentLine[1])
        if str(currentLine[0]) == "up":
            depth -=int(currentLine[1])
        if str(currentLine[0]) == "down":
            depth +=int(currentLine[1])

    return posX*depth
        

def ex2(input : list[str]) -> int:
    posX = 0
    depth = 0
    aim = 0
    for i in range(len(lines)):
        currentLine = lines[i].split(" ")
        if str(currentLine[0]) == "forward":
            posX += int(currentLine[1])
            depth += aim*int(currentLine[1])
        if str(currentLine[0]) == "up":
            aim -=int(currentLine[1])
        if str(currentLine[0]) == "down":
            aim +=int(currentLine[1])

    return posX*depth


file = open("Day2/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
