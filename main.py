from pm import Pm
from st import St
from pt import Pt
import sys

if (__name__ == "__main__"):
    initFile = open(sys.argv[1], 'r')
    inputFile = open(sys.argv[2], 'r')
    outputFile = open('output-dp.txt', 'w')

    pm = Pm()
    lines = initFile.readlines()
    pm.addSegments(lines[0].strip())
    pm.addPages(lines[1].strip())

    for i in inputFile.readline().split():
        s = int(i) >> 18
        w = int(i) & 511
        p = (int(i) >> 9) & 511
        try:
            result = pm.lookup(s,p,w)
            outputFile.write(str(result) + ' ')
        except ValueError:
            outputFile.write('-1 ')

    initFile.close()
    inputFile.close()
    outputFile.close()