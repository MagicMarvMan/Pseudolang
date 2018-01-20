import engine

class Parser(engine.Engine):
    def getStrippedMultiLineString(self, str):
        return str.splitlines()

    def getPartsOfString(self, str):
        return str.split(" ")
