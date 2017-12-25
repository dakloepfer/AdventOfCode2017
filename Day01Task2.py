
number = input("Give the input. ");

digits = [int(d) for d in str(number)]; # more efficient would be an implementation that uses repeated subtraction and division by 10, but this is shorter and works

sum = 0;

stepsize = len(digits) / 2; # can assume even number of digits according to question

for i in range(0, len(digits)):
    if (digits[i] == digits[(i+stepsize)%len(digits)]):
        sum += digits[i];
        

print sum; 
    