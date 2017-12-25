

def reallocate(current_distr):
    
    largest_ind = 0;
    most_blocks = current_distr[0];
    
    for i in range(1, len(current_distr)):
        if current_distr[i] > most_blocks:
            largest_ind = i;
            most_blocks = current_distr[i];
    
    current_distr[largest_ind] = 0;
    j = (largest_ind+1) % len(current_distr);
    blocks_to_distr = most_blocks;
    
    while blocks_to_distr > 0:
        current_distr[j] += 1;
        blocks_to_distr = blocks_to_distr - 1;
        j = (j+1) % len(current_distr);
    
    return current_distr;
    
def equal(a, b):
    if len(a) != len(b): return False;
    output = True;
    
    for i in range(0, len(a)):
        if a[i]!=b[i]:
            output = False;
            break;
        
    return output;


file = open("adventofcode_day6.txt");
input = file.read();
file.close();

current_distr = list(map(int, list(input.split())));

    

all_distr = [list(current_distr)];

counter = 0;
already_seen = False;

while not already_seen:
    current_distr = reallocate(current_distr);
    counter += 1;
    
    for i in range(0, len(all_distr)):
        if equal(current_distr, all_distr[i]):
            already_seen = True;
            print "Distribution seen again after " + str(counter - i) + " reallocations."
            break;
        
    all_distr.append(list(current_distr));

print counter;
    
    



    
