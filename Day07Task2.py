from StdSuites.Type_Names_Suite import null



class Node:
    
    def __init__(self, line):
        
        line = line.replace('(', '');
        line = line.replace(')', '');
        line = line.replace(',', '');
        input = list(line.split());

        self.name = input[0];
        
        self.weight = int(input[1]);
        
        self.childrennames = input[3:len(input)];

        self.parentname = "";
        
        self.children = list();
        
        self.parent = null;
        
    def addChildren(self, nodes):
        for i in range(0, len(nodes)):
            if nodes[i].name in self.childrennames:
                self.children.append(nodes[i]);
                nodes[i].addParent(self);
            
            
    def addParent(self, node):
        self.parent = node;
        
    
    def getsubtreeweight(self):
        w = self.weight;
        
        for i in range(0, len(self.children)):
            w += self.children[i].getsubtreeweight();
            
        return w;    
    
    def equalsubtrees(self):
        
        subweights = list();
        
        for i in range(0, len(self.children)):
            subweights.append(self.children[i].getsubtreeweight());

        if len(self.children) == 0: 
            return null;
        
        different = False;
        for i in range(1, len(subweights)):
            if subweights[i] != subweights[0]:
                different = True;
                if i > 1: 
                    return self.children[i];
                
                elif subweights[i] == subweights[(i+1)%len(subweights)]:
                    return self.children[0];
                
                else: 
                    return self.children[i];
                break;
        if not different: return null;
     
def findbadnode(node):
    
    if node.equalsubtrees() == null:
        return node;
        
    subtree = node.equalsubtrees();
    return findbadnode(subtree);
 
        
def getroot(nodes):
    for i in range(0, len(nodes)):
        if nodes[i].parent == null:
            return nodes[i];
        

    

file = open("adventofcode_day7.txt");
puzzleinput = file.read();
file.close();
puzzleinput = list(puzzleinput.split('\n'));

nodes = list();


for i in range(0, len(puzzleinput)):
    nodes.append(Node(puzzleinput[i]));

for i in range(0, len(nodes)):
    nodes[i].addChildren(nodes);


root = getroot(nodes);
badnode = findbadnode(root);

delta = 0;
p = badnode.parent;
i = 0;
while delta == 0:
    delta = badnode.getsubtreeweight() - p.children[i].getsubtreeweight();
    i += 1; 

print badnode.weight - delta;

        
        
                
        
        
        
        