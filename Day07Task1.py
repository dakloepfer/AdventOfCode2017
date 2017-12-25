from StdSuites.Type_Names_Suite import null


class Node:

    def __init__(self, line):
        
        line = line.replace('(', '');
        line = line.replace(')', '');
        input = list(line.split());

        self.name = input[0];
        
        self.weight = input[1];
        
        self.children = input[3:len(input)];
        
        self.parent = null;
        
        
def addParents(nodes, children, name):
    for i in range(0, len(nodes)):
        if nodes[i].name in children:
            nodes[i].parent = name;

        
    
           
    
file = open("adventofcode_day7.txt");
puzzleinput = file.read();
file.close();
puzzleinput = list(puzzleinput.split('\n'));

nodes = list();

for i in range(0, len(puzzleinput)):
    nodes.append(Node(puzzleinput[i]));
    
for i in range(0, len(nodes)):
    for j in range(0, len(nodes[i].children)):
        addParents(nodes, nodes[i].children[j], nodes[i].name);
        
for i in range(0, len(nodes)):
    if nodes[i].parent == null:
        print nodes[i].name;
        break;
    

    