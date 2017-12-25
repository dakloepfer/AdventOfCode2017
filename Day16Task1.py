
global array;

def performSpin(X):
    
    return array[-X:] + array[:-X];
    
def performExchange(A, B):
    
    helper = array[A];
    array[A] = array[B];
    array [B] = helper;
    
def performPartner(A, B):
    
    x = -1;
    y = -1;
    
    foundA = False;
    foundB = False;
    for i in range(0, len(array)):
        if foundA and foundB: break;
        
        if array[i] == A:
            x = i;
            foundA = True;
        if array[i] == B:
            y = i;
            foundB = True;
        
    performExchange(x, y);

    
file = open("adventofcode_day16.txt");
puzzleinput = file.read();
file.close();

puzzleinput = puzzleinput.split(',');

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'];

for i in range(0, len(puzzleinput)):

    if puzzleinput[i][0] == 's':
        array = performSpin(int(puzzleinput[i][1:]));
    elif puzzleinput[i][0] == 'x':
        if puzzleinput[i][2] == '/':
            performExchange(int(puzzleinput[i][1]), int(puzzleinput[i][3:]));
        else:
            performExchange(int(puzzleinput[i][1:3]), int(puzzleinput[i][4:]));

    else:
        performPartner(puzzleinput[i][1], puzzleinput[i][3]);

        
result = array[0];

for i in range(1, len(array)):
    result = result + array[i];
print result;    




