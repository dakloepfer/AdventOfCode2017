
with open("adventofcode_day2.txt") as input:
    spreadsh = [line.strip().split('\t') for line in input]#;
    
spreadsh = [map(int, row) for row in spreadsh];

checksum = 0;

for i in range(0, len(spreadsh)):
    
    for j in range(0, len(spreadsh[i])):
        for k in range(0, len(spreadsh[i])):
            if j == k: continue;
            
            if (spreadsh[i][j]%spreadsh[i][k]==0):
                checksum += spreadsh[i][j]/spreadsh[i][k]; # If we assume only one possible pair per row, we can skip to the next row once we have found it
                
                
print checksum;