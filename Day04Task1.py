

with open("adventofcode_day4.txt") as input:
    phrases = [line.strip().split() for line in input];
    

counter = 0;
valid = True;

for i in range(0, len(phrases)):
    valid = True;
    for j in range(0, len(phrases[i])):
        for k in range(j+1, len(phrases[i])):
            if phrases[i][j] == phrases[i][k]: # luckily python makes string comparison very easy
                valid = False;
                break;
                break;
            
    if valid: counter +=1;        
    
print counter;

