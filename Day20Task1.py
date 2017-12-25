from json.encoder import INFINITY

# I suppose to get the long term it is easiest to just simulate the particles for a while 
# A correct algorithm would have to check for LOADS of special cases CFCalendarGetComponentDifference

class particle:
    
    def __init__(self, line):
        
        line = line.replace('p', '');
        line = line.replace('v', '');
        line = line.replace('a', '');
        line = line.replace('=', '');
        line = line.replace('<', '');
        line = line.replace('>', '');
        line = line.replace(' ', '');
        
        line = line.split(',');
        line = [float(n) for n in line];

        self.p = [line[0], line[1], line[2]];
        self.v = [line[3], line[4], line[5]];
        self.a = [line[6], line[7], line[8]];

    
    def update(self):
        
        for i in range(0, 3):
            self.v[i] = self.v[i] + self.a[i];
            self.p[i] = self.p[i] + self.v[i];

    def getDistance(self):
        
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2]);
    

    def jumpForward(self, t): # here I don't use the bad Euler method to simulate but use the fact that this problem is easily solvable -  in the long run it shouldn't matter about which particle is closest to origin
        
        for i in range(0, 3):

            self.p[i] = self.p[i] + t * self.v[i] + 0.5*t*t * self.a[i];
            self.v[i] = self.v[i] + t * self.a[i]; 
    
    
    
file = open("adventofcode_day20.txt");
puzzleinput = file.read();
file.close();

input = puzzleinput.split('\n');

particles = list();

for i in range(0, len(input)):
    
    particles.append(particle(input[i]));
    
    particles[i].jumpForward(10000);
    
min_dist = INFINITY;
min_index = -1;    
    
for i in range(0, len(particles)):
    
    if abs(particles[i].getDistance()) < min_dist:
        min_dist = abs(particles[i].getDistance());
        min_index = i;
      
print min_index;

## This is the code to simulate the particles 

# for i in range(0, 10000):
#     for i in range(0, len(particles)):
#         
#         particles[i].update();
#         
# min_dist = INFINITY;
# min_index = -1;    
#     
# for i in range(0, len(particles)):
#     
#     if abs(particles[i].getDistance()) < min_dist:
#         min_dist = abs(particles[i].getDistance());
#         min_index = i;
#       
# print min_index;


