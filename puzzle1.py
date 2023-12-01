inputFile = 'input.txt'

def openFile(inputFileLoc):
  f = open(inputFileLoc, "r")

  return f

def getcodes(inputFile):
  codes = []
  for line in inputFile:
    code = getCode(line)
    codes.append(code)

  return codes

def getCode(line):
  first = line[0:1]
  last = line[-1]

  return first + last