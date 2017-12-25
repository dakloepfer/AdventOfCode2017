
global layers;
global my_depth;

# generally this implementation is not the fastest one, but it is easier to read, write and understand

class Layer:
    
    def __init__(self, line):
        
        line = line.replace(':', '');
        line = line.split();
        
        self.index = int(line[0]);
        self.range = int(line[1]);
        
def am_I_caught(layer_index):
    
    caught = False;
    
    if layers[layer_index].index % (2*layers[layer_index].range -2) == 0:
        return True;
    
    return caught;
    
    

file = open("adventofcode_day13.txt");
puzzleinput = file.read();
file.close();

puzzleinput = list(puzzleinput.split('\n'));

layers = list();

for i in range(0, len(puzzleinput)):
    layers.append(Layer(puzzleinput[i])); # by not storing empty layers I have opted for a space-efficient but not time-efficient implementation

severity = 0;
    


for i in range(0, len(layers)):
   
    if am_I_caught(i):
        severity += layers[i].index * layers[i].range;
    
print severity;




