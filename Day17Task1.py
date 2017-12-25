
step_size = 343;

array = [0];

current_index = 0;

for i in range(1, 2018):
    
    current_index = (current_index + step_size) % len(array);
    current_index += 1;

    array.insert(current_index, i);
    

    
print array[(current_index + 1) % len(array)];    
    