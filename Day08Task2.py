

class Register:
    
    
    def __init__(self, name, value):
        
        self.name = name;
        
        self.value = value;
        


class Instruction:
    
    def __init__(self, line):
        
        input = list(line.split());

        self.reg_op_name = input[0];
        
        self.action = input[1];
        
        self.delta = int(input[2]);
        
        self.reg_con_name = input[4];
        
        self.con_bool = input[5];
        
        self.con_val = int(input[6]);
        

        
def alreadyentered(regs, name):
    seen = False;
    for i in range(0, len(regs)):
        if regs[i].name == name:
            seen = True;
            break;
        
    return seen;
            
        
def apply_instr(regs, instr):
    op_reg_ind = -1;
    con_reg_ind = -1;
    for i in range(0, len(regs)):
        if regs[i].name == instr.reg_op_name: op_reg_ind = i;
        if regs[i].name == instr.reg_con_name: con_reg_ind = i;
        
    bool_expr = False;
    
    if instr.con_bool == "==":
        bool_expr = regs[con_reg_ind].value == instr.con_val;
    elif instr.con_bool == "!=":
        bool_expr = regs[con_reg_ind].value != instr.con_val;  
    elif instr.con_bool == ">":
        bool_expr = regs[con_reg_ind].value > instr.con_val;
    elif instr.con_bool == "<":
        bool_expr = regs[con_reg_ind].value < instr.con_val;
    elif instr.con_bool == ">=":
        bool_expr = regs[con_reg_ind].value >= instr.con_val;
    elif instr.con_bool == "<=":
        bool_expr = regs[con_reg_ind].value <= instr.con_val;
    
    if bool_expr:
        if instr.action == "inc":
            regs[op_reg_ind].value += instr.delta;
            
        else: 
            regs[op_reg_ind].value -= instr.delta;
    
    
    

file = open("adventofcode_day8.txt");
puzzleinput = file.read();
file.close();
puzzleinput = list(puzzleinput.split('\n'));


instrs = list();

for i in range(0, len(puzzleinput)):
    instrs.append(Instruction(puzzleinput[i]));

regs = list();

for i in range(0, len(instrs)):
    if not alreadyentered(regs, instrs[i].reg_op_name):
        regs.append(Register(instrs[i].reg_op_name, 0));
    if not alreadyentered(regs, instrs[i].reg_con_name):
        regs.append(Register(instrs[i].reg_con_name, 0));
   
max = 0;
for i in range(0, len(instrs)):
    apply_instr(regs, instrs[i]);
    
    # I could update that without the for loop by only looking at the value of the node just updated, but 
    # that would need me storing the indices of the registers operated on in the instruction class which would need 
    # as many for loops as this here does.
    for j in range(0, len(regs)):
        if regs[j].value > max:
            max = regs[j].value;


        
print max;        

        
    
    
    



