# in an interest of increasing speed, I switch to represent array as a string

file = open("adventofcode_day16.txt");
puzzleinput = file.read();
file.close();

moves = puzzleinput.split(',');

array =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'];

arrays = list();
n = 0;
m = 0;

for i in range(0, 10000): # 10000 should be enough to encompass the cycle
    
    a = ''.join(array);
    found = False;
    for k in range(0, len(arrays)): 
        if arrays[k] == a:
            n = i; 
            m = k;
            found = True;
            break;
    if found: break;    
    else: arrays.append(a);  
    
    for j in range(0, len(moves)):
        
        if moves[j][0] == 's':
            array = array[-int(moves[j][1:]):] + array[:-int(moves[j][1:])];
        elif moves[j][0] == 'x':
            a,b = map(int, moves[j][1:].split('/'))
            array[a], array[b] = array[b], array[a];
    
        else:
        
            x = array.index(moves[j][1]);
            y = array.index(moves[j][3]);
                
            array[x], array[y] = array[y], array[x];
            
          
    
    
reps = (1000000000-m) % (n-m);
array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'];

for i in range(0, reps):
    for j in range(0, len(moves)):
        
        if moves[j][0] == 's':
            array = array[-int(moves[j][1:]):] + array[:-int(moves[j][1:])];
        elif moves[j][0] == 'x':
            a,b = map(int, moves[j][1:].split('/'))
            array[a], array[b] = array[b], array[a];
    
        else:
        
            x = array.index(moves[j][1]);
            y = array.index(moves[j][3]);
                
            array[x], array[y] = array[y], array[x];

result = array[0];

for i in range(1, len(array)):
    result = result + array[i];
print result;    