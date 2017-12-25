

global tape;
global current_index;
global state;
global checksum;


def moveleft():
    
    global current_index;
    global tape;
    
    if current_index == 0:
        tape.insert(0, False);
    else: current_index -= 1;
    
def moveright():
    
    global current_index;
    global tape;
  
    if current_index == len(tape)-1:
        tape.append(False);
    
    current_index += 1;
    
def performStep():
    
    global tape;
    global current_index;
    global state;
    global checksum;

    if state == 'A':
        
        if tape[current_index] == False: 
            tape[current_index] = True;
            moveright();
            state = 'B';
            checksum += 1;
        else: 
            tape[current_index] = False;
            moveleft();
            state = 'C';
            checksum -= 1;
    
    elif state == 'B':
        
        if tape[current_index] == False: 
            tape[current_index] = True;
            moveleft();
            state = 'A';
            checksum += 1;
        else: 
            moveright();
            state = 'C';
            
    elif state == 'C':
        
        if tape[current_index] == False:
            tape[current_index] = True;
            moveright();
            state = 'A';
            checksum += 1;
        else:
            tape[current_index] = False;
            moveleft();
            state = 'D';
            checksum -= 1;
            
    elif state == 'D':
        
        if tape[current_index] == False:
            tape[current_index] = True;
            moveleft();
            state = 'E';
            checksum += 1;
        else:
            moveleft();
            state = 'C';
            
    elif state == 'E':
        
        if tape[current_index] == False:
            tape[current_index] = True;
            moveright();
            state = 'F';
            checksum += 1;
        else:
            moveright();
            state = 'A';
    
    else:
        
        if tape[current_index] == False:
            tape[current_index] = True;
            moveright();
            state = 'A';
            checksum += 1;
        else:
            moveright();
            state = 'E';        
    
tape = [False];
current_index = 0;
state = 'A';
checksum = 0;

i = 0; 

while i < 12261543:
    
    performStep();
    i += 1;

print checksum;
