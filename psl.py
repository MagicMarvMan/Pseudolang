import pseudolang
import sys

if len(sys.argv) > 0:
    pseudol = pseudolang.Pseudolang()
    pseudol.executeCommand(sys.argv[0])
else:
    print("Error: No command supplied!")
