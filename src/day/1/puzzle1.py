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
  first = line[0:1]
  last = line[-2]

  return first + last

def main(): 
    file = openFile(inputFile)
    codes = getCodes(file)

    for code in codes:
       print(code)
  
if __name__=="__main__": 
    main() 