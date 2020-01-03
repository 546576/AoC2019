#variables
filepath = 'day_2/opcode.txt'
position = [0, 1, 2, 3]
opcode_array = []
opcode_reset = opcode_array
position_reset = position
verb = 0
noun = 0
output_iteration = 0
iteration = 0

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
operator_1 = opcode_array[position[0]]
operator_2 = opcode_array[position[1]]
operator_3 = opcode_array[position[2]]
operator_4 = opcode_array[position[3]]

#output check function
def output_check():
    if opcode_array[0] == 19690720:
        print('noun equals: ', opcode_array[1])
        print('verb equals: ', opcode_array[2])


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
        iteration += 1

    noun += 1

print('final opcode output: ', opcode_array[0])
print('total iterations: ', iteration)
fp.close()


