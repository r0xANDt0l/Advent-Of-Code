def ex1(input : list[str]) -> int:
    nCul = len(input[0]) -1
    bitarray = [0 for i in range(nCul)]
    for i in range(len(lines)):
        for a in len[bitarray]:
            if str(lines[a]) == "0":
                bitarray[a] -= 1
            else:
                bitarray[a] += 1


def ex2(input : list[str]) -> int:
    pass


file = open("Day3/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
