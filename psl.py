import pseudolang
import sys

if len(sys.argv) > 1:
    pseudol = pseudolang.Pseudolang()
    pseudol.executeCommand(sys.argv[1])
else:
    print("Error: No command supplied!")
