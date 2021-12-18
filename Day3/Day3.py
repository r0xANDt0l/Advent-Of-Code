def ex1(input : list[str]) -> int:
    nCul = len(input[0]) -1
    bitarray = [0 for i in range(nCul)]
    for i in input:
        for j in range(nCul):
            if i[j] == "0":
                bitarray[j] -= 1
            else:
                bitarray[j] += 1
				
    g = ""
    e = ""
    for i in bitarray:
        if i > 0:
            g+="1"
            e+="0"
        else:
            g+="0"
            e+="1"
    return int(g,2) * int(e,2)

def discrim():
    nCul = len(input[0]) -1
    bitarray = [0 for i in range(nCul)]
    for i in input:
        for j in range(nCul):
            if i[j] == "0":
                bitarray[j] -= 1
            else:
                bitarray[j] += 1

def ex2(input : list[str])-> int:

    O2 = discrim(input,True)

    CO2 = discrim(input,False)

    return int(O2,2) * int(CO2,2)


file = open("Day3/dataTest.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
