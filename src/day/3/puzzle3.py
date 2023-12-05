class Coord:
    xMin = 0
    yMin = 0
    xMax = 0
    yMax = 0

class Symbol:
    x = 0
    y = 0

class Part:
    isPart = True
    # All the coords a symbol could be in
    coords = Coord()

    def containsSymbol(self, symbol: Symbol):
        if symbol.x > self.coords.xMax | symbol.x < self.coords.xMin:
            return False
        elif symbol.y > self.coords.yMax | symbol.y < self.coords.yMin:
            return False
            






