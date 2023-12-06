import re

inputFile = 'input/day/3/input.txt'

class Coord:
    xMin = 0
    yMin = 0
    xMax = 0
    yMax = 0

class Symbol:
    x = 0
    y = 0

class Part:
    def __init__(self):
        self.isPart = False
        # All the coords a symbol could be in
        self.coords = Coord()
        self.value = 0

    def containsSymbol(self, symbol: Symbol):
        if symbol.x > self.coords.xMax or symbol.x < self.coords.xMin:
            return False
        elif symbol.y > self.coords.yMax or symbol.y < self.coords.yMin:
            return False
        else:
            self.isPart = True
            return True
        
class LineResult:
    def __init__(self):
        self.parts = []
        self.symbols = []
        self.value = 0

def createSymbols(symbols, line: str, y) -> list[Symbol]:
    lastIndex = 0
    symbolObjs = []

    for symbol in symbols:
        symbolObj = Symbol()
        index = line.index(symbol, lastIndex)

        symbolObj.x = index
        symbolObj.y = y
        symbolObjs.append(symbolObj)

        lastIndex = index + 1

    return symbolObjs

def createParts(parts, line: str, y) -> list[Part]:
    lastIndex = 0
    partsObjs =[]

    for part in parts:
        partObj = Part()
        index = line.index(part, lastIndex)

        partObj.coords.xMin = index - 1
        partObj.coords.xMax = index + len(part)
        partObj.coords.yMin = y - 1
        partObj.coords.yMax = y + 1

        partObj.value = int(part)

        partsObjs.append(partObj)

        lastIndex = index + len(part)

    return partsObjs
    
def processLine(line, y, prevSymbols, prevParts):
    lineResult = LineResult()
    
    parts = re.findall('[0-9]+', line)
    symbols = re.findall('\*|\#|\$|\+|\-|\@|\=|\&|\%|\/', line)

    symbolObjs = createSymbols(symbols, line, y)
    partObjs = createParts(parts, line, y)

    lineResult.parts = partObjs
    lineResult.symbols = symbolObjs

    symbolObjs.extend(prevSymbols)
    partObjs.extend(prevParts)

    lineSum = 0

    for partObj in partObjs:
        # don't check parts that have already been confirmed
        if not partObj.isPart:
            for symbolObj in symbolObjs:
                if partObj.containsSymbol(symbolObj):
                    lineSum += partObj.value
                    break
    
    lineResult.value = lineSum

    return lineResult

def openFile(inputFileLoc):
    f = open(inputFileLoc, "r")

    return f

def main():
    # run puzzle
    file = openFile(inputFile)

    sum = 0
    y = 0
    prevParts = []
    prevSymbols = []

    for line in file:
        lineResult = processLine(line, y, prevSymbols, prevParts)
        prevParts = lineResult.parts
        prevSymbols = lineResult.symbols

        sum += lineResult.value
        y += 1

    result = sum 
    
    print(result)
  
if __name__=="__main__": 
    main() 



