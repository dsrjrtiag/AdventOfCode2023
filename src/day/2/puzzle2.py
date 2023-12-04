import re

inputFile = 'input/day/2/input.txt'

colors = ['blue', 'red', 'green']
maxRed = 12
maxGreen = 13
maxBlue = 14

class Game:
    gameId = 0
    gameString = ''

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def getGames(file):
    games = []
    for line in file:
        game = Game()
        game.gameId = int(re.search('[0-9]+', line).group(0))
        game.gameString = line
        
        games.append(game)

    return games

def gameIsPossible(game: Game):
    scores = game.gameString[game.gameString.index(str(game.gameId)) + 3:]
    draws = scores.split(';')
    
    for draw in draws:
        if not drawIsPossible(draw):
            return False
        
    return True
        
            
def drawIsPossible(draw):
    colorScores = draw.split(',')

    for colorScore in colorScores:
        split = colorScore.strip().split(' ')
        score = split[0]
        color = split[1]

        if color == 'blue' and int(score) > maxBlue:
            return False
        elif color == 'green' and int(score) > maxGreen:
            return False
        elif color == 'red' and int(score) > maxRed:
            return False
    return True

def main(): 
    file = openFile(inputFile)
    games = getGames(file)

    gameSum = 0
    for game in games:
        if gameIsPossible(game):
            gameSum += game.gameId

    print(gameSum)
  
if __name__=="__main__": 
    main() 