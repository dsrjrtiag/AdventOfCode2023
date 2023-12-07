inputFile = 'input/day/4/input.txt'

def calcScore(wins: int):
    if wins > 0:
        return pow(2, wins - 1)
    else:
        return 0
    
class Game:
    def __init__(self, cardNum, winningNums, drawnNums):
        self.cardNum = cardNum
        self.winningNums = winningNums
        self.drawnNums = drawnNums

    def getWins(self):
        wins = 0
        for drawnNum in self.drawnNums:
            if drawnNum in self.winningNums:
                wins += 1

        return wins
    
def processLine(line: str, games: [], lines: []):
    splitLine = line.split(':')
    cardNum = splitLine.split()[1].strip()
    input = splitLine[1].strip()

    splitInput = input.split('|')

    winningNums = splitInput[0].strip().split()
    drawnNums = splitInput[1].strip().split()

    games.add(Game(cardNum, winningNums, drawnNums))

    wins = 0
    for drawnNum in drawnNums:
        if drawnNum in winningNums:
            wins += 1

    return wins

def getGame(line: str):
    splitLine = line.split(':')
    cardNum = splitLine[0].split()[1].strip()
    input = splitLine[1].strip()

    splitInput = input.split('|')

    winningNums = splitInput[0].strip().split()
    drawnNums = splitInput[1].strip().split()

    return Game(cardNum, winningNums, drawnNums)

def processGame(game, games):
    wins = game.getWins()
    totalGames = [game]
    if wins > 0:
        nextGameIndex = int(game.cardNum)

        for x in range(nextGameIndex, nextGameIndex + wins):
            totalGames.extend(processGame(games[x], games))
    
    return totalGames

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def main():
    # run puzzle
    file = openFile(inputFile)

    lines = file.readlines()

    games = []
    for line in lines:
        game = getGame(line)

        games.append(game)

    totalGames = []

    for game in games:
        totalGames.extend(processGame(game, games.copy()))

    result = len(totalGames)
    print(result)



if __name__=="__main__": 
    main() 

