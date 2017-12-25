

file = open("adventofcode_day9.txt");
puzzleinput = file.read();
file.close();

i=0;
while i < len(puzzleinput):
    c = puzzleinput[i];
    
    if c == '!':
        puzzleinput = puzzleinput[:i] + puzzleinput[(i+2):];
    else: i+=1;
     
total = 0;     
i1 = 0;   
while i1 < len(puzzleinput):
    
    c = puzzleinput[i1];
    
    if c == '<':
        i2 = i1;
        while puzzleinput[i2] != '>':
            i2+=1;
            
        puzzleinput = puzzleinput[:i1] + puzzleinput[(i2+1):];
        total += (i2-i1-1);
        
    else: i1 += 1;
    
print total;