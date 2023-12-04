import re

inputFile = 'input/day/1/input.txt'

def openFile(inputFileLoc):
  f = open(inputFileLoc, "r")

  return f

def getCodes(inputFile):
  codes = []
  for line in inputFile:
    code = getCode(line)
    codes.append(code)

  return codes

def getCode(line):
  first = re.findall('[0-9]', line)[0]
  last = re.findall('[0-9]', line)[-1]

  return int(first + last)

def main(): 
    file = openFile(inputFile)
    codes = getCodes(file)

    print(sum(codes))
  
if __name__=="__main__": 
    main() 