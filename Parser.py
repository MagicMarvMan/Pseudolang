from Engine import *

class Parser(Engine):
    def getStrippedMultiLineString(self, str):
        return str.splitlines()

    def getPartsOfString(self, str):
        return str.split(" ")
