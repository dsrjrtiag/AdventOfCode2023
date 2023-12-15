inputFile = 'input/day/5/input.txt'

class Ratio:
    def __init__(self, dest, source, length):
        self.dest = dest
        self.source = source
        self.length = length

def processRatio(inputs, ratios : [Ratio]):
    outputs = []
    for input in inputs:
        appended = False
        for ratio in ratios:
            if input >= ratio.source and input < ratio.source + ratio.length:
                outputs.append(ratio.dest + (input - ratio.source))
                appended = True
                break
            # else:
            #     outputs.append(input)
        if not appended:
            outputs.append(input)

    return outputs

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def readSeeds(line: str):
    seeds = []

    inputs = list(map(int, line.split()[1:]))
    for index, input in enumerate(inputs):
        seeds.append(inputs[index])
        index+=1
        

    return seeds

def readRatio(line: str):
    values = line.split()
    return Ratio(int(values[0]), int(values[1]), int(values[2]))


def main():
    # run puzzle
    file = openFile(inputFile)

    outputs = readSeeds(file.readline())
    ratios = []

    for line in file:
        if line[0].isdigit():
            ratios.append(readRatio(line))
        else:
            if len(ratios) > 0:
                outputs = processRatio(outputs, ratios)
                ratios = []

    outputs = processRatio(outputs, ratios)
    outputs.sort()
    result = outputs
    print(result)
  
if __name__=="__main__": 
    main() 

