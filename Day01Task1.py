
number = input("Give the input. "); # only give integers as input

digits = [int(d) for d in str(number)]; # more efficient would be an implementation that uses repeated subtraction and division by 10, but this is shorter and works

sum = 0;

for i in range(0, len(digits)):
    if (digits[i] == digits[(i+1)%len(digits)]):
        sum += digits[i];
        

print sum;
    