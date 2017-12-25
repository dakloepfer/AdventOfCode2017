

current_a = input("Give the starting A value: ");
current_b = input("Give the starting B value: ");

a_factor = 16807;
b_factor = 48271;

n = 40000000;

divisor = 2147483647;

counter = 0;

for i in range(0, n):
    
    current_a = (current_a * a_factor)%divisor;
    current_b = (current_b * b_factor)%divisor;
    
    if (current_a % 65536) ^ (current_b % 65536) == 0: # want smallest 16 bits only, so compare after modulus with 2^16
        counter += 1;
  
print counter;

