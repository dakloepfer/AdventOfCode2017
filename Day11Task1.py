

file = open("adventofcode_day11.txt");
puzzleinput = file.read();
file.close();

steps = puzzleinput.split(',');

e1 = 0; # n
e2 = 0; # ne

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
        

# turn axial into cube coordinates, then calculate distance easily
x = e1;
y = e2;
z = -e1-e2;

steps_required = int(0.5*(abs(x) + abs(y) + abs(z)));

print steps_required;





