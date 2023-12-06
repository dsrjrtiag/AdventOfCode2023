inputFile = 'input/day/4/input.txt'

def calcScore(wins: int):
    if wins > 0:
        return pow(2, wins - 1)
    else:
        return 0
    
def processLine(line: str):
    input = line.split(':')[1].strip()

    splitInput = input.split('|')

    winningNums = splitInput[0].strip().split()
    drawnNums = splitInput[1].strip().split()

    wins = 0
    for drawnNum in drawnNums:
        if drawnNum in winningNums:
            wins += 1

    return wins

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def main():
    # run puzzle
    file = openFile(inputFile)

    totalScore = 0

    for line in file:
        wins = processLine(line)
        totalScore += calcScore(wins)

    result = totalScore
    print(result)

if __name__=="__main__": 
    main() 

