global rules;
global pattern;
global helperpattern;

class Rule:
    
    
    def __init__(self, line):
        
        line = line.replace('=> ', '');
        line = line.split();
        
        self.orig = line[0];
        self.transf = line[1];
        
        self.orig = self.orig.split('/');
        self.transf = self.transf.split('/');
  
def flip_hor(square):
    
    s = square[::-1];
    return s; 

def flip_ver(square):
    
    s = [r[::-1] for r in square];
    return s;
  
def rotate(square):
    s = list();
    for i in range(len(square)-1, -1, -1):
        r = "";
        for j in range(0, len(square)):
            r = r + square[j][i];
        s.append(r);
        
    return s;
            
      
  
def find_and_apply_rule(square, row, origsize):
    
    global rules;
    global pattern;
    global helperpattern;
    
    for r in rules:
        
        if square == r.orig:
            square = r.transf;
            break;
        elif rotate(square) == r.orig:
            square = r.transf;
            break;
        elif rotate(rotate(square)) == r.orig:
            square = r.transf;
            break;
        elif rotate(rotate(rotate(square))) == r.orig:
            square = r.transf;
            break;
        elif flip_ver(square) == r.orig:
            square = r.transf;
            break;
        elif flip_hor(square) == r.orig: # == rotate(rotate(flip_ver(square)))
            square = r.transf;
            break;
        elif rotate(flip_ver(square)) == r.orig:
            square = r.transf;
            break;
        elif rotate(flip_hor(square)) == r.orig:
            square = r.transf;
            break;
        
    
    size = origsize + 1;
    if len(helperpattern) == row * size:
        
        for s in square: helperpattern.append(s);
        
    else: 
        if size == 3:
            helperpattern[row*size] = helperpattern[row*size] + square[0];
            helperpattern[row*size+1] = helperpattern[row*size+1] + square[1];
            helperpattern[row*size+2] = helperpattern[row*size+2] + square[2];
            
        else: # size == 4
            helperpattern[row*size] = helperpattern[row*size] + square[0];
            helperpattern[row*size+1] = helperpattern[row*size+1] + square[1];
            helperpattern[row*size+2] = helperpattern[row*size+2] + square[2];
            helperpattern[row*size+3] = helperpattern[row*size+3] + square[3];


  
def step():
    
    global rules;
    global pattern;
    global helperpattern;
        
    if len(pattern) % 2 == 0:
        
        for i in range(0, len(pattern)/2):
            for j in range(0, len(pattern)/2):
                
                subsquare = [pattern[2*i][(2*j) : (2*j+2)], pattern[2*i + 1][(2*j) : (2*j + 2)]];
                
                find_and_apply_rule(subsquare, i, 2); 
                
    else: 
        
        for i in range(0, len(pattern)/3):
            for j in range(0, len(pattern)/3):
                
                subsquare = [pattern[3*i][(3*j) : (3*j+3)], pattern[3*i + 1][(3*j) : (3*j + 3)], pattern[3*i + 2][(3*j) : (3*j + 3)]];
            
                find_and_apply_rule(subsquare, i, 3);
          
    pattern = helperpattern;
    helperpattern = list();
    
def countActive():
    
    global rules;
    global pattern;
    global helperpattern;
        
    counter = 0;  
    for r in pattern:
        for c in r:
        
            if c == '#': counter += 1;
            
    return counter;
 
def printPattern():
    patternstring="";
    for r in pattern:
        patternstring = patternstring + r + "\n";
        
    print patternstring;

file = open("adventofcode_day21.txt");
puzzleinput = file.read();
file.close();

puzzleinput = puzzleinput.split('\n');
    
rules = list();

for l in puzzleinput:
    rules.append(Rule(l));
    
pattern = [".#.", "..#", "###"];     
helperpattern = list();  

for i in range(0, 5):
    step();
    
    
print countActive();
printPattern();



    