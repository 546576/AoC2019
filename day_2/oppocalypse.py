#variables
filepath = 'day_2/opcode.txt'
position = [0, 1, 2, 3]
opcode_array = []

#setting up the opcode_array and writing the file contents into it
with open(filepath) as fp:
        line = fp.readline()
        final_tally = 0
        n = 0

        while line:
            line_int = int(line)

            opcode_array.insert(n, line_int)
            line = fp.readline()
            n += 1

#adjusting opcode_array positions
opcode_array[1] = 12
opcode_array[2] = 2
operator_1 = opcode_array[position[0]]
operator_2 = opcode_array[position[1]]
operator_3 = opcode_array[position[2]]
operator_4 = opcode_array[position[3]]

#running opcode
while operator_1 != 99:
    operator_1 = opcode_array[position[0]]
    operator_2 = opcode_array[position[1]]
    operator_3 = opcode_array[position[2]]
    operator_4 = opcode_array[position[3]]

    if operator_1 == 1:
        add_op = opcode_array[operator_2] + opcode_array[operator_3]
        opcode_array[operator_4] = add_op
        position[0] += 4
        position[1] += 4
        position[2] += 4
        position[3] += 4

    elif operator_1 == 2:
        multiply_op = opcode_array[operator_2] * opcode_array[operator_3]
        opcode_array[operator_4] = multiply_op
        position[0] += 4
        position[1] += 4
        position[2] += 4
        position[3] += 4

print(opcode_array[0])
fp.close()