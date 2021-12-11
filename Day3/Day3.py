def ex1(input : list[str]) -> int:
    for i in range(len(lines)):
        binIN = lines[i]
        binOUT = int(binIN, 2)

def ex2(input : list[str]) -> int:
    pass


file = open("Day3/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
