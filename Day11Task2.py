

def getDistanceToOrigin(e1, e2):
    
    return int(0.5*(abs(e1) + abs(e2) + abs(-e1-e2)));


file = open("adventofcode_day11.txt");
puzzleinput = file.read();
file.close();

steps = puzzleinput.split(',');

e1 = 0;
e2 = 0;
max_dist = 0;

for s in steps:
    
    if s == 'n':
        e1 += 1;
    elif s == 'ne':
        e2 += 1;
    elif s == 'se':
        e1 -= 1;
        e2 += 1;
    elif s == 's':
        e1 -= 1;
    elif s == 'sw':
        e2 -= 1;
    else:
        e1 += 1;
        e2 -= 1;
    
    if getDistanceToOrigin(e1, e2) > max_dist:
        max_dist = getDistanceToOrigin(e1, e2);
        
        
print max_dist;
        
