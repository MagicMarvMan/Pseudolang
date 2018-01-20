import engine
import parser
import reader

class Commands(engine.Engine):

    def mainCommand(self, args):
        cmd = args[1]

        if cmd == "v":
            return "Pseudolang Alpha-0.1"
        else:
            return "Unknown command!"
