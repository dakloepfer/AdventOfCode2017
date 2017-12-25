# not the prettiest of algorithms but I think it does the job
from numpy import ceil;

n = input("Enter the position. ");

spiral = 0;
    
if n == 1: 
    distance = 0;
    print distance;
    quit();
    
spiral = ceil(sqrt(n));
if spiral%2 == 0:
    spiral+=1;
        
spiral = 0.5*(spiral-1);
        

m = (n-(2*spiral -1)*(2*spiral-1) -1)%(2*spiral); # n is m steps away from first thing in spiral

m -= spiral-1; # m is now distance of n from element closest to 1 in spiral

distance = spiral; # initialize distance with position of closest element of spiral

distance += abs(m);

print distance;


