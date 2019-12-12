#reading the file and writing the contents to an array
import math
filepath = 'day_1/input.txt'


with open(filepath) as fp:
        line = fp.readline()
        final_tally = 0

        while line:
            line_int = float(line)
            X = (line_int/3)
            X2 = math.floor(X)
            X3 = X2-2
            final_tally += X3

            while X3 > 0:

                X = (X3 / 3)
                X2 = math.floor(X)
                X3 = X2 - 2
                if X3 > 0:
                    final_tally += X3

            line = fp.readline()

        print(final_tally)

fp.close()