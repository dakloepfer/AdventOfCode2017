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
    
    if grid[posy][posx] == 'i':
        if dir == -1:
            dir = 2;
        elif dir == 2: 
            dir = 1;
        elif dir == 1:
            dir = -2;
        else: 
            dir = -1;
            
        grid[posy][posx] = 'f';
        
        moveForward();
        
    elif grid[posy][posx] == 'c':
        if dir == -1:
            dir = -2;
        elif dir == -2:
            dir = 1;
        elif dir == 1:
            dir = 2;
        else:
            dir = -1;
            
        grid[posy][posx] = 'w';
        
        moveForward();
    
    elif grid[posy][posx] == 'w':
        grid[posy][posx] = 'i';
        counter += 1;
        moveForward();
        
    else: # flagged
        dir = -dir;
        
        grid[posy][posx] = 'c';
        
        moveForward();
        
def moveForward():
    global grid;
    global posx;
    global posy;
    global dir; 
       
    if posx == 0:
        for r in grid:
            r.appendleft('c');
            posx = 1;
            
    elif posx+1 == len(grid[0]):
        for r in grid:
            r.append('c');
            
    if posy == 0:
        grid.appendleft(deque(['c']*len(grid[0])));
        posy = 1;
    
    elif posy+1 == len(grid):
        grid.append(deque(['c']*len(grid[0])));
            
    if abs(dir) == 1:
        posy += dir;
    else:
        posx += dir/2;
        
        

file = open("adventofcode_day22.txt");
puzzleinput = file.read();
file.close();

puzzleinput = puzzleinput.split('\n');
    
# c == clean, i == infected, w == weakened, f == flagged
grid = deque();

for r in puzzleinput:
    row = deque();
    for c in r:
        if c == '.':
            row.append('c');
        else: row.append('i');
        
    grid.append(row);


counter = 0;
# assume square map input
posx = len(grid)/2;
posy = len(grid)/2;
dir = -1; # -1 = north, 1 = south, 2 = east, -2 = west

    
i = 0;
while i < 10000000:
    burst();
    i += 1;
     
print counter;      
print len(grid)
print len(grid[0])