import engine
import parser as pars

class Reader(engine.Engine):

    parser = pars.Parser()

    def readFileWithLines(self, path):
        rv = ""
        with open(path,"r") as file:
            rv = self.parser.getStrippedMultiLineString(file.read())
            file.close()
        return rv
