import re

inputFile = 'input/day/1/input.txt'

digits = {'one': '1',
          'two': '2',
          'three': '3',
          'four': '4',
          'five': '5',
          'six': '6',
          'seven': '7',
          'eight': '8',
          'nine': '9'}

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
  found = re.findall('(?=([0-9]|' + '|'.join(digits.keys()) + '))', line)
  first = digits.get(found[0]) or found[0]
  last = digits.get(found[-1]) or found[-1]

  return int(first + last)

def main(): 
    file = openFile(inputFile)
    codes = getCodes(file)

    print(sum(codes))
  
if __name__=="__main__": 
    main() 