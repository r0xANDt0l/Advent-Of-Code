def ex1(input : list[str]) -> int:
# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

# The diagnostic report (your puzzle input) consists of a list of binary numbers which,
# when decoded properly, can tell you many useful things about the conditions of the submarine.
# The first parameter to check is the power consumption.

# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate).
# The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers
# in the diagnostic report. For example, given the following diagnostic report:    
    
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. 
# What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
    bitarray = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(lines)):
        for a in len[bitarray]:
            if str(lines[a]) == "0":
                bitarray[a] -= 1
            else:
                bitarray[a] += 1
    return bitarray  


def ex2(input : list[str]) -> int:
    pass


file = open("Day3/data.txt")

lines = file.readlines()

print(ex1(lines))
print(ex2(lines))
