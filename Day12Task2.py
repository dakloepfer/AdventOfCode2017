
global vertices;
vertices = list();


class Node:
    
    visited = False;
    
    def __init__(self, line):
        line = line.replace(',', '');
        line = line.split();
        self.index = int(line[0]);
        self.adjacent = list();
        
    def addAdjacents(self, line):
        
        line = line.replace(',', '');
        line = line.split();
        
        for i in range(2, len(line)):
            self.adjacent.append(vertices[int(line[i])]);
            
    
    

def DFS(startindex):
    
    S = list();
    S.append(vertices[startindex]);
    
    while len(S) != 0:
        
        v = S.pop();
        
        if v.visited == False:
            v.visited = True;
            for w in v.adjacent:
                S.append(w);
        


file = open("adventofcode_day12.txt");
puzzleinput = file.read();
file.close();
    
puzzleinput = list(puzzleinput.split('\n'));


for i in range(0, len(puzzleinput)):
    
    vertices.append(Node(puzzleinput[i]));

for i in range(0, len(puzzleinput)):
    
    vertices[i].addAdjacents(puzzleinput[i]);
    
counter = 0;
for i in range(0, len(vertices)):
    
    if not vertices[i].visited:    
        counter += 1;
        DFS(i);
        
print counter;
    
    
            
    
    
    