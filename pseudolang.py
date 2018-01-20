import engine
import parser
import reader
import commands

class Pseudolang(engine.Engine):

    cmds = commands.Commands()

    def executeCommand(self, args):
        print(self.cmds.mainCommand(args))
