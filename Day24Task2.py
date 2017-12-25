from _collections import defaultdict

global components;
global bridges;

def add_bridges(bridge):
    global components;
    global bridges;
    
    bridge = bridge or [(0, 0)];
    
    latest = bridge[-1][1];
    
    for c in components[latest]:
        
        if not ((latest, c) in bridge or (c, latest) in bridge): # assumes no duplicated components which is true for my input; if there are duplicates, just have another dictionary that counts how many of a component are left
            
            newbridge = bridge + [(latest, c)]; 
            
            bridges.append(newbridge);
            
            add_bridges(newbridge);
            
def getBridgeStrength(bridge):
    result = 0;
    for c in bridge:
        result += c[0] + c[1];
        
    return result;
                
       
file = open("adventofcode_day24.txt");
puzzleinput = file.read();
file.close();

components = defaultdict(set)

for l in puzzleinput.strip().splitlines():
    pin1, pin2 = [int(p) for p in l.split('/')];
    components[pin1].add(pin2);
    components[pin2].add(pin1);

bridges = [];

add_bridges(None);

maxlength = 0;
maxstrength = 0;


for b in bridges: 
    if len(b) > maxlength: 
        maxlength = len(b);
        maxstrength = getBridgeStrength(b);
        
    elif len(b) == maxlength:
        if getBridgeStrength(b) > maxstrength:
            maxstrength = getBridgeStrength(b);
            
print maxstrength;
        
    
