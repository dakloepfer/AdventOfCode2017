from collections import deque

global grid;
global counter; 
global posx;
global posy;
global dir;

def burst():
    global grid;
    global counter; 
    global posx;
    global posy;
    global dir;
    
    if grid[posy][posx]:
        if dir == -1:
            dir = 2;
        elif dir == 2: 
            dir = 1;
        elif dir == 1:
            dir = -2;
        else: 
            dir = -1;
            
        grid[posy][posx] = False;
        
        moveForward();
        
    else:
        if dir == -1:
            dir = -2;
        elif dir == -2:
            dir = 1;
        elif dir == 1:
            dir = 2;
        else:
            dir = -1;
            
        grid[posy][posx] = True;
        counter += 1;
        
        moveForward();
        
    
def moveForward():
    global grid;
    global posx;
    global posy;
    global dir; 
       
    if posx == 0:
        for r in grid:
            r.appendleft(False);
            posx = 1;
            
    elif posx+1 == len(grid[0]):
        for r in grid:
            r.append(False);
            
    if posy == 0:
        grid.appendleft(deque([False]*len(grid[0])));
        posy = 1;
    
    elif posy+1 == len(grid):
        grid.append(deque([False]*len(grid[0])));
            
    if abs(dir) == 1:
        posy += dir;
    else:
        posx += dir/2;
        

            
    
             
    
    
    
    

file = open("adventofcode_day22.txt");
puzzleinput = file.read();
file.close();

puzzleinput = puzzleinput.split('\n');
    
    
grid = deque();

for r in puzzleinput:
    row = deque();
    for c in r:
        if c == '.':
            row.append(False);
        else: row.append(True);
        
    grid.append(row);


counter = 0;
# assume square map input
posx = len(grid)/2;
posy = len(grid)/2;
dir = -1; # -1 = north, 1 = south, 2 = east, -2 = west

    
i = 0;
while i < 10000:
     burst();

     i += 1;
     
print counter;      