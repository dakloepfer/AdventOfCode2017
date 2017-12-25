

file = open("adventofcode_day9.txt");
puzzleinput = file.read();
file.close();

i=0;
while i < len(puzzleinput):
    c = puzzleinput[i];
    
    if c == '!':
        puzzleinput = puzzleinput[:i] + puzzleinput[(i+2):];
    else: i+=1;
     
i1 = 0;   
while i1 < len(puzzleinput):
    
    c = puzzleinput[i1];
    
    if c == '<':
        i2 = i1;
        while puzzleinput[i2] != '>':
            i2+=1;
            
        puzzleinput = puzzleinput[:i1] + puzzleinput[(i2+1):];
        
    else: i1 += 1;

i = 0;            
while i < len(puzzleinput):
    c = puzzleinput[i];
    
    if c != '{' and c != '}':
        puzzleinput = puzzleinput[:i] + puzzleinput[(i+1):];
    else: i+=1;
        
total = 0;    
current_level = 1;
for i, c in enumerate(puzzleinput):
    if c == '{':
        total += current_level;
        current_level += 1;
    elif c == '}':
        current_level -= 1;
    
print total;
    
    

            
                
