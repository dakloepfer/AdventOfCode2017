


def Hashround(array, instrs, current_pos, skip_size):
    
    upper = 0;
    
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
            
            
    return array, current_pos, skip_size;
    

file = open("adventofcode_day10.txt");
puzzleinput = file.read();
file.close();

instrs = list();
array = range(0, 256);
current_pos = 0;
skip_size = 0;

for c in puzzleinput:
    
    instrs.append(ord(c));
    
instrs.append(17);
instrs.append(31);
instrs.append(73);
instrs.append(47);
instrs.append(23);

for i in range(0, 64):
    
    ret = Hashround(array, instrs, current_pos, skip_size);
    array = ret[0];
    current_pos = ret[1];
    skip_size = ret[2];
    

dense = list();


for i in range(0, 16):
    dense.append(0)
    for j in range(16*i, 16*(i+1)):
        dense[i] = dense[i] ^ array[j];

hexcode = [hex(n) for n in dense];
hash = '';


for i in range(0, len(hexcode)):
    s = hexcode[i];
    if len(s) >= 4:
        hash = hash + hexcode[i][2:];
    else:
        hash = hash + '0' + hexcode[i][2:];
        

        
print hash;
        


