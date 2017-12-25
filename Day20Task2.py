
global particles;

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
    

def resolve_collisions():
    
    i = 0;
    while i < len(particles):
        to_delete = list();
        for j in range(i+1, len(particles)):
            
            if particles[i].p[0] == particles[j].p[0] and particles[i].p[1] == particles[j].p[1] and particles[i].p[2] == particles[j].p[2]:
                to_delete.append(j);
            
        if len(to_delete) > 0:
            for j in range(len(to_delete)-1, -1, -1):
                del particles[to_delete[j]];
            
            del particles[i];
        
        else: i+=1;
            
    
file = open("adventofcode_day20.txt");
puzzleinput = file.read();
file.close();

input = puzzleinput.split('\n');

particles = list();

for i in range(0, len(input)):
    
    particles.append(particle(input[i]));
    
# To get the same collisions they get, I probably do need to simulate the particles. For now I will also assume that the particles only collide if their positions exactly match
# at one of the times we simulate the particles (and that swapping places in between need not have them collide)

for i in range(0, 1000):
    for i in range(0, len(particles)):
         
        particles[i].update();
        
    resolve_collisions();
        
print len(particles);

