

step_size = 343;

length = 1;

current_index = 0;

max = 0;

for i in range(1, 50000001):
    
    current_index = (current_index + step_size) % length;
    current_index += 1;
    
    if current_index == 1: max = i;
    
    length += 1;

print max; 
    