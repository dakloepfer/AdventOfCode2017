
from numpy import floor, zeros, sqrt, ceil

def getcoords(z):
    n=z+1;
    spiral = 0;
    if n==1: 
        n_y_coord = 0;
        n_x_coord = 0;
        
    elif n != 1:
        spiral = ceil(sqrt(n));
        if spiral%2 == 0:
            spiral+=1;
        
        spiral = 0.5*(spiral-1);
        
        m = (n-(2*spiral -1)*(2*spiral-1) -1)%(2*spiral); # n is m steps away from first number in its part of the spiral
        
        m -= spiral-1; # m is now distance of n from element closest to 1 in spiral

        quadr = floor((n-(2*spiral -1)*(2*spiral-1) -1)/(2*spiral));

        if quadr == 0: 
            n_y_coord = m;
            n_x_coord = spiral;
            
        if quadr == 1:
            n_x_coord = -m;
            n_y_coord = spiral;
            
        if quadr == 2:
            n_y_coord = -m;
            n_x_coord = -spiral;
            
        if quadr == 3:
            n_x_coord = m;
            n_y_coord = -spiral;
            
    return [n_x_coord, n_y_coord];
    

def getindex(x, y):
    if y*y >= x*x:
        index = 4*y*y -y-x;
        if y<x:
            index -= 2*(y-x);
    
    else:
        index = 4*x*x -y-x;
        if y<x:
            index += 2*(y-x);
            
    return index;
    
    
    
h = input("Enter the input. ");


cells = zeros((100*h, 1));
cells[0] = 1; 
 
for i in range(1, h):
    h_coord = getcoords(i);
    h_x_coord = h_coord[0];
    h_y_coord = h_coord[1];
    cells[i] = cells[getindex(h_x_coord, h_y_coord+1)] + cells[getindex(h_x_coord, h_y_coord-1)] + cells[getindex(h_x_coord+1, h_y_coord)] + cells[getindex(h_x_coord-1, h_y_coord)] + cells[getindex(h_x_coord+1, h_y_coord+1)] + cells[getindex(h_x_coord-1, h_y_coord+1)] + cells[getindex(h_x_coord+1, h_y_coord-1)] + cells[getindex(h_x_coord-1, h_y_coord-1)];
    if cells[i] > h:
        print i, cells[i];
        break;
 
     
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


