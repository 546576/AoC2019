#reading the file and writing the contents to an array
import math
filepath = 'Day1/input.txt'


with open(filepath) as fp:
        line = fp.readline()
        finaltally = 0

        while line:
            lineint = float(line)
            X = (lineint/3)
            X2 = math.floor(X)
            X3 = X2-2
            finaltally = finaltally + X3
            line = fp.readline()

        print(finaltally)

fp.close()