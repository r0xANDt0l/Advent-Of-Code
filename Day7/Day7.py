def ex1(input: list[str]) -> int:
    crabs = input[0].split(',')

    min = float('inf')

    for i in range(2000):
        counter = 0
        for j in crabs:
            counter += abs(i - int(j))
        if counter < min:
            min = counter
    
    return min


def ex2(input: list[str]) -> int:
    crabs = input[0].split(',')

    min = float('inf')

    for i in range(2000):
        counter = 0
        for j in crabs:
            distance = abs(i - int(j))
            counter += (distance * (distance + 1))/2
        if counter < min:
            min = counter
    
    return int(min)

file = open("Day7/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))