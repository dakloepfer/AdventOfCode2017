
global regs;
global instrs;
global counter;

def performInstruction(current_instr):
    
    global regs;
    global instrs;
    global counter;
    
    instr = instrs[current_instr];
    
    if current_instr < 0 or current_instr >= len(instrs): return;
    
    if instr[0] == "set":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]] = regs[instr[2]];
        else:        
            regs[instr[1]] = int(instr[2]);
    
        return current_instr + 1;
        
    
    elif instr[0] == "sub":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]] -= regs[instr[2]];
        else:        
            regs[instr[1]] -= int(instr[2]);
     
        return current_instr + 1;

    elif instr[0] == "mul":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]] *= regs[instr[2]];
        else:        
            regs[instr[1]] *= int(instr[2]);
            
        counter += 1;
        return current_instr + 1;

           
    elif instr[0] == "jnz":
        if not instr[1].replace('-', '').isdigit():
            if not regs[instr[1]] == 0:
                
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
        else:
            if not int(instr[1]) == 0:
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
               
        return current_instr + 1;
    
            
file = open("adventofcode_day23.txt");
puzzleinput = file.read();
file.close();
instrs = list(puzzleinput.split('\n'));

regs = {};

for i in range(0, len(instrs)):
    instrs[i] = list(instrs[i].split());
    
    if instrs[i][1] not in regs:
        if not instrs[i][1].replace('-', '').isdigit():
            regs[instrs[i][1]] = 0;

current_instr = 0;
counter = 0;

while not (current_instr < 0 or current_instr >= len(instrs)):
    
    current_instr = performInstruction(current_instr);


print counter; 