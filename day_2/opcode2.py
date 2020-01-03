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

#creating a copy of the basic array to reset to
opcode_reset = opcode_array
position_reset = position

#output check function
def output_check():
    if opcode_array[0] == 521344:
        print('noun equals: ', opcode_array[1])
        print('verb equals: ', opcode_array[2])

#adjusting opcode_array positions
verb = 0
noun = 0
operator_1 = opcode_array[position[0]]
operator_2 = opcode_array[position[1]]
operator_3 = opcode_array[position[2]]
operator_4 = opcode_array[position[3]]

#setting up verb/noun loops
while noun < 100:
    opcode_array[1] = noun
    verb = 0

    while verb < 100:
        opcode_array[2] = verb

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
                output_check()

            elif operator_1 == 2:
                multiply_op = opcode_array[operator_2] * opcode_array[operator_3]
                opcode_array[operator_4] = multiply_op
                position[0] += 4
                position[1] += 4
                position[2] += 4
                position[3] += 4
                output_check()


        opcode_array = opcode_reset
        position = position_reset
        verb += 1

    noun += 1

print('final opcode output: ', opcode_array[0])
fp.close()


