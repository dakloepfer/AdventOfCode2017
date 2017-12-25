

file = open("adventofcode_day10.txt");
puzzleinput = file.read();
file.close();

instrs = list(int(number) for number in puzzleinput.strip().split(','));

array = range(0, 256);

current_pos = 0;
upper = 0;
skip_size = 0;

for i in range(0, len(instrs)):
    
    upper = (current_pos + instrs[i])%len(array);
    
    if instrs[i] == 0 or instrs[i] == 1:
        
        current_pos = (upper + skip_size)%len(array);
        skip_size += 1;
        continue;
    
    if upper > current_pos:
        
        array = array[:current_pos] + list(reversed(array[current_pos:upper])) + array[upper:];
        current_pos = (upper + skip_size)%len(array);
        skip_size += 1;
        
    elif upper <= current_pos: 
        
        sublist = array[current_pos:] + array[:upper];
        sublist = list(reversed(sublist));
        
        array = sublist[(len(array)-current_pos):] + array[upper:current_pos] + sublist[:(len(array)-current_pos)];
        
        current_pos = (upper + skip_size)%len(array);
        skip_size += 1;
        
        

print array[0]*array[1];
        