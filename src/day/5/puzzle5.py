inputFile = 'input/day/5/input.txt'

class Ratio:
    def __init__(self, dest, source, length):
        self.dest = dest
        self.source = source
        self.length = length

def processRatio(inputs, ratio : Ratio):
    outputs = []
    for input in inputs:
        if input >= ratio.source and input < ratio.source + ratio.length:
            outputs.append(input + (ratio.dest - ratio.source))
        else:
            outputs.append(input)

    return outputs

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def readSeeds(line: str):
    seeds = []

    seeds = list(map(int, line.split()[1:]))

    return seeds

def readRatio(line: str):
    values = line.split()
    return Ratio(int(values[0]), int(values[1]), int(values[2]))


def main():
    # run puzzle
    file = openFile(inputFile)

    outputs = readSeeds(file.readline())

    for line in file:
        if line[0].isdigit():
            ratio = readRatio(line)
            outputs = processRatio(outputs, ratio)
    outputs.sort()
    result = outputs
    print(result)
  
if __name__=="__main__": 
    main() 

