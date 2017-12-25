
with open("adventofcode_day5.txt") as input:
    instr = [int(line) for line in input]#;
    
current_ind = 0;
counter = 0;

while current_ind>=0 and current_ind<len(instr):

    instr[current_ind] += 1;
    current_ind += instr[current_ind]-1;

    counter += 1;

print counter;