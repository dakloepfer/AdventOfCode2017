
with open("adventofcode_day5.txt") as input:
    instr = [int(line) for line in input]#;
    
current_ind = 0;
past_ind = 0;
counter = 0;

while current_ind>=0 and current_ind<len(instr):
    past_ind = current_ind;
    current_ind += instr[current_ind];

    if instr[past_ind] >= 3:
        instr[past_ind] -= 1;
    else: instr[past_ind] += 1;
    
    counter += 1;

print counter;