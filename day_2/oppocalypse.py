#reading the file and writing the contents to an array
filepath = 'day_2/opcode.txt'
array_position = [0, 1, 2, 3]
array = []


#setting up the array
with open(filepath) as fp:
        line = fp.readline()
        final_tally = 0
        n = 0

        while line:
            line_int = int(line)

            array.insert(n, line_int)
            line = fp.readline()
            n += 1



#adjusting array positions
op_1 = array[array_position[0]]
op_2 = array[array_position[1]]
op_3 = array[array_position[2]]
op_4 = array[array_position[3]]
array[1] = 12
array[2] = 2

#running opcode

while op_1 != 99:

    if op_1 == 1:
        add_op = array[op_2] + array[op_3]
        array[op_4] = add_op
        array_position[0] += 4
        array_position[1] += 4
        array_position[2] += 4
        array_position[3] += 4


    elif op_1 == 2:
        add_op = array[op_2] * array[op_3]
        array[op_4] = add_op
        array_position[0] += 4
        array_position[1] += 4
        array_position[2] += 4
        array_position[3] += 4


print(array[0])





fp.close()