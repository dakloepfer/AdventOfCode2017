
# There might be a smarter algorithm than just exhaustively trying every possibility, but that is prohibitively hard to code
# This implementation runs into trouble if no solution is guaranteed
global layers;
global max_depth;
# generally this implementation is not the fastest one, but it is easier to read, write and understand

class Layer:
    
    def __init__(self, line):
        
        line = line.replace(':', '');
        line = line.split();
        
        self.index = int(line[0]);
        self.range = int(line[1]);
              
def am_I_caught(delay):
    
    caught = False;
    d = 0;
    for i in range(0, len(layers)):
        d = delay + layers[i].index;
        
        if d % (2*layers[i].range - 2) == 0:
            
            return True;
        
    return caught;
    

file = open("adventofcode_day13.txt");
puzzleinput = file.read();
file.close();

puzzleinput = list(puzzleinput.strip().split('\n'));

layers = list();

for i in range(0, len(puzzleinput)):
    layers.append(Layer(puzzleinput[i])); # by not storing empty layers I have opted for a space-efficient but not time-efficient implementation

delay = 0;


while am_I_caught(delay):
    delay += 1;
    
print delay;

