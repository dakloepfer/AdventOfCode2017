from collections import deque

global instrs;
global regs0;
global regs1;
global queue0;
global queue1;
global counter;
global noData;

def performInstruction0(current_instr):
    
    instr = instrs[current_instr];
    
    if current_instr < 0 or current_instr >= len(instrs): return;
    
    if instr[0] == "set":
        
        if not instr[2].replace('-', '').isdigit():
            regs0[instr[1]] = regs0[instr[2]];
        else:        
            regs0[instr[1]] = int(instr[2]);
    
        return current_instr + 1;
        
    elif instr[0] == "snd":
        
        if not instr[1].replace('-', '').isdigit():
            queue1.append(regs0[instr[1]]);
        else:        
            queue1.append(int(instr[1]));
        noData[1] = False;
    
        return current_instr + 1;
    
    elif instr[0] == "add":
        
        if not instr[2].replace('-', '').isdigit():
            regs0[instr[1]] += regs0[instr[2]];
        else:        
            regs0[instr[1]] += int(instr[2]);
     
        return current_instr + 1;

    elif instr[0] == "mul":
        
        if not instr[2].replace('-', '').isdigit():
            regs0[instr[1]] *= regs0[instr[2]];
        else:        
            regs0[instr[1]] *= int(instr[2]);
            
        return current_instr + 1;
    
    elif instr[0] == "mod":
        
        if not instr[2].replace('-', '').isdigit():
            regs0[instr[1]] = regs0[instr[1]] % regs0[instr[2]];
        else:        
            regs0[instr[1]] = regs0[instr[1]] % int(instr[2]);
        
        return current_instr + 1;

           
    elif instr[0] == "jgz":
        if not instr[1].replace('-', '').isdigit():
            if regs0[instr[1]] > 0:
                
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs0[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
        else:
            if int(instr[1]) > 0:
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs0[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
               
        return current_instr + 1;
    
    else: # rcv
        if not len(queue0) == 0:
            regs0[instr[1]] = queue0.popleft();
            return current_instr + 1;
        else: 
            noData[0] = True;
            return current_instr;
            

def performInstruction1(current_instr):
    
    instr = instrs[current_instr];
    
    if current_instr < 0 or current_instr >= len(instrs): return;
    
    if instr[0] == "set":
        
        if not instr[2].replace('-', '').isdigit():
            regs1[instr[1]] = regs1[instr[2]];
        else:        
            regs1[instr[1]] = int(instr[2]);
    
        return current_instr + 1;
        
    elif instr[0] == "snd":
        
        if not instr[1].replace('-', '').isdigit():
            queue0.append(regs1[instr[1]]);
        else:        
            queue0.append(int(instr[1]));
        counter[0] += 1;
        noData[0] = False;
        return current_instr + 1;
    
    elif instr[0] == "add":
        
        if not instr[2].replace('-', '').isdigit():
            regs1[instr[1]] += regs1[instr[2]];
        else:        
            regs1[instr[1]] += int(instr[2]);
     
        return current_instr + 1;

    elif instr[0] == "mul":
        
        if not instr[2].replace('-', '').isdigit():
            regs1[instr[1]] *= regs1[instr[2]];
        else:        
            regs1[instr[1]] *= int(instr[2]);
            
        return current_instr + 1;
    
    elif instr[0] == "mod":
        
        if not instr[2].replace('-', '').isdigit():
            regs1[instr[1]] = regs1[instr[1]] % regs1[instr[2]];
        else:        
            regs1[instr[1]] = regs1[instr[1]] % int(instr[2]);
        
        return current_instr + 1;

           
    elif instr[0] == "jgz":
        if not instr[1].replace('-', '').isdigit():
            if regs1[instr[1]] > 0:
                
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs1[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
        else:
            if int(instr[1]) > 0:
                if not instr[2].replace('-', '').isdigit():
                    return current_instr + regs1[instr[2]];
                else:        
                    return current_instr + int(instr[2]);
               
        return current_instr + 1;
    
    else: # rcv
        if not len(queue1) == 0:
            regs1[instr[1]] = queue1.popleft();
            return current_instr + 1;
        else: 
            noData[1] = True;
            return current_instr;


file = open("adventofcode_day18.txt");
puzzleinput = file.read();
file.close();
instrs = list(puzzleinput.split('\n'));

regs0 = {};
regs1 = {};

queue0 = deque([]);
queue1 = deque([]);

counter = [0];

for i in range(0, len(instrs)):
    instrs[i] = list(instrs[i].split());
    
    if instrs[i][1] not in regs0:
        if not instrs[i][1].replace('-', '').isdigit():
            regs0[instrs[i][1]] = 0; 
            regs1[instrs[i][1]] = 0; 

regs1["p"] = 1;

current_instr0 = 0;
current_instr1 = 0;

noData = [False, False];

while current_instr0 >= 0 and current_instr0 < len(instrs) and current_instr1 >= 0 and current_instr1 < len(instrs):
    
    if noData[0] and noData[1]: break;
    
    current_instr0 = performInstruction0(current_instr0);
    current_instr1 = performInstruction1(current_instr1);


print counter;



