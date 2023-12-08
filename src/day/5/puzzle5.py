inputFile = 'input/day/5/input.txt'

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def readSeeds(line: str):
    seeds = []

    seeds = line.split()[1:]

    return seeds

def map(input: []):
    return input

def main():
    # run puzzle
    file = openFile(inputFile)

    seeds = readSeeds(file.readline())

    result = seeds
    print(result)
  
if __name__=="__main__": 
    main() 

