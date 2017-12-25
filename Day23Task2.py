from math import sqrt, ceil

# This only works for the input; I would have liked to build an algorithm that detects loops and 
# uses some clever trickery to fast-forward those, but that turned out to be rather hard when trying to 
# consider all the different cases that can happen and that one would have to check for. 

# Instead the way to go is to analyze the instructions and see what they actually mean. 
# First, b and c get initialized to: 

b0 = 108100;
c = b0 + 17000;

# The bit until the jump instruction jnz g -8 is a loop; d is constant, e gets incremented each time. The loop breaks 
# when e == b. In between, if e*d = e*2 == b; (i.e. b is not prime) we set f to 0 
# (it was set to 1 before). This last bit is done using the jnz g 2 instruction. 

# This whole spiel gets repeated with increasing d, until d == b to make sure we set f to 0 even if b is not even. 
# It is essentially two nested for loops, the outer one increasing d, the inner one increasing e and checking whether
# d * e == b, setting f = 0 if yes. It is quite a wasteful implementation, since one could stop when one has found 
# a single pair of d, e but the for loops keep going until the end. 

# If we have found such a pair d, e, we have f = 0 so we increase h by 1. 
# The next three instructions check if b == c, if yes it quits, if not we increase b by 17 and go back to just after
# the first initialization. 

# So h counts the number of bs in the range b0 = 108100 to c = b0 + 17000 with step size 17 that can be represented
# by two natural numbers d*e = b, i.e. the number of non prime numbers among those. 

h = 0;

for b in range(b0, c+1, 17):

    for x in range(2, int(ceil(sqrt(b)))):
        if b % x == 0: 
            h += 1; 
            break;
    
print h;


    