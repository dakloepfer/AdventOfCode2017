
global regs;
#global current_instr;
global instrs;


def performInstruction(current_instr):
    
    instr = instrs[current_instr];
    
    if current_instr < 0 or current_instr >= len(instrs): return;
    
    if instr[0] == "set":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]][0] = regs[instr[2]][0];
        else:        
            regs[instr[1]][0] = int(instr[2]);
    
        return current_instr + 1;
        
    elif instr[0] == "snd":
        
        regs[instr[1]][1] = regs[instr[1]][0];
    
        return current_instr + 1;
    
    elif instr[0] == "add":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]][0] += regs[instr[2]][0];
        else:        
            regs[instr[1]][0] += int(instr[2]);
     
        return current_instr + 1;

    elif instr[0] == "mul":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]][0] *= regs[instr[2]][0];
        else:        
            regs[instr[1]][0] *= int(instr[2]);
            
        return current_instr + 1;
    
    elif instr[0] == "mod":
        
        if not instr[2].replace('-', '').isdigit():
            regs[instr[1]][0] = regs[instr[1]][0] % regs[instr[2]][0];
        else:        
            regs[instr[1]][0] = regs[instr[1]][0] % int(instr[2]);
        
        return current_instr + 1;

           
    elif instr[0] == "jgz":
        if not instr[1].replace('-', '').isdigit():
            if regs[instr[1]][0] > 0:
                
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs[instr[2]][0];
                else:        
                    return current_instr + int(instr[2]);
        else:
            if int(instr[1]) > 0:
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs[instr[2]][0];
                else:        
                    return current_instr + int(instr[2]);
               
        return current_instr + 1;
    
    else:
        if not regs[instr[1]][0] == 0:
            print regs[instr[1]][1];
            if  not regs[instr[1]][1] == 0:
                return current_instr + len(instrs);
        return current_instr + 1;
            
file = open("adventofcode_day18.txt");
puzzleinput = file.read();
file.close();
instrs = list(puzzleinput.split('\n'));

regs = {};

for i in range(0, len(instrs)):
    instrs[i] = list(instrs[i].split());
    
    if instrs[i][1] not in regs:
        if not instrs[i][1].replace('-', '').isdigit():
            regs[instrs[i][1]] = [0, 0]; # first number is value of register, second number is last sound played by it


current_instr = 0;

while not (current_instr < 0 or current_instr >= len(instrs)):
    
    current_instr = performInstruction(current_instr);
    