
from json.encoder import INFINITY

global current;
global diag;
global letters; # for this task I don't actually need the letters, but it seems nice to keep them around
global current_dir;
global steps;

def turn():
    
    global letters;
    global current_dir;
    global current;
    global steps;
    mincounter = INFINITY;
    dir = 0;
    
    counter = 0;
    for i in range(current[0]-1, -1, -1): # try north
        if abs(current_dir) == 1: break;
        
        if diag[i][current[1]] == ' ': break;
        
        if diag[i][current[1]] == '+' or diag[i][current[1]] == '|':
            if mincounter > counter: 
                mincounter = counter;
                dir = 1;
            break;
        
        counter += 1;
        
      
    counter = 0;            
    for i in range(current[0]+1, len(diag)): # try south

        if abs(current_dir) == 1: break;
        if diag[i][current[1]] == ' ': break;
        
        if diag[i][current[1]] == '+' or diag[i][current[1]] == '|':
            if mincounter > counter: 
                mincounter = counter;
                dir = -1;
            break;
        
        counter += 1;

        
        
    counter = 0;
    for i in range(current[1]+1, len(diag[current[0]])): # try east

        if abs(current_dir) == 2: break;
        
        if diag[current[0]][i] == ' ': break;
        
        if diag[current[0]][i] == '+' or diag[current[0]][i] == '-':
            if mincounter > counter: 
                mincounter = counter;
                dir = 2;
            break;
        
        counter += 1;

  
        
    counter = 0;    
    for i in range(current[1]-1, -1, -1): # try west

        if abs(current_dir) == 2: break;
        if diag[current[0]][i] == ' ': break;
        
        if diag[current[0]][i] == '+' or diag[current[0]][i] == '-': 
            if mincounter > counter: 
                mincounter = counter;
                dir = -2;   
            break;
        

    current_dir = dir;
    
    if dir == 1:
        current[0] -= 1;
    elif dir == -1:
        current[0] += 1;
    elif dir == 2:
        current[1] += 1;
    elif dir == -2:
        current[1] -= 1;
        

def moveForward():
    
    global current;
    global letters;
    global steps;
    
    while not (current[0]>=len(diag) or current[0]<0 or current[1] >= len(diag[0]) or current[1] < 0):
        
        if diag[current[0]][current[1]] == '+': 
            turn();
            steps += 1;
        elif diag[current[0]][current[1]] == ' ': break;
        
        if diag[current[0]][current[1]].isalpha():
            letters.append(diag[current[0]][current[1]]);
            diag[current[0]] = diag[current[0]][:current[1]] + ' ' + diag[current[0]][(current[1]+1):];
            
        if current_dir == 1:
            current[0] -= 1;
        elif current_dir == -1:
            current[0] += 1;
        elif current_dir == 2:
            current[1] += 1;
        elif current_dir == -2:
            current[1] -= 1;  
              
        steps += 1;
        


file = open("adventofcode_day19.txt");
puzzleinput = file.read();
file.close();

diag = list(puzzleinput.split('\n'));

start = [0, 0];

for i in range(0, len(diag[0])):
    if diag[0][i] == '|':
        start[1] = i;
        break;
    
current = start;
letters = list();
current_dir = -1; # 1 = N, -1 = S, 2 = E, -2 = W
steps = 0;

moveForward();

print letters;
print steps;