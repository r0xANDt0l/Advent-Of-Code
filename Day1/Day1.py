#check how many times the subgoes down

def ex1(input : list[str]) -> int:
    result = 0
    lastNumb = int(input[0])

    for i in input:
        if int(i) > lastNumb:
            result +=1
        lastNumb = int(i)

    return result

def ex2(input : list[str]) -> int:
    result = 0
    lastNumb = int(input[0]) + int(input[1]) + int(input[2])

    for i in range(len(input) -2):
        groupCurr = int(input[i]) + int(input[i+1]) + int(input[i+2])
        if groupCurr > lastNumb:
            result +=1
            lastNumb = groupCurr
        lastNumb = groupCurr

    return result   


file = open("Day1/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
