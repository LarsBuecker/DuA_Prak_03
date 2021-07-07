import os
import sys

from datetime import datetime

now = datetime.now()
os.system("python main.py " + sys.argv[1] + " > output.txt.sol")
print("Time: " + str(datetime.now() - now))

output = open("output.txt.sol", "r")
sol = open(sys.argv[1] + ".sol", "r")

outline = []
for line in output:
    outline.append(line)
solline = []
for line in sol: 
    solline.append(line)

for i in range(0, len(solline) - 1):
    tokens = solline[i].split(" ")
    if tokens[0] == "#":
        continue
    assert solline[i] == outline[i], "Ouput is not identical with solution at line " + str(i)