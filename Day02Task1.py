

with open("adventofcode_day2.txt") as input:
    spreadsh = [line.strip().split('\t') for line in input]#;
    
spreadsh = [map(int, row) for row in spreadsh];

checksum = 0;

for i in range(0, len(spreadsh)):
    max_row = max(spreadsh[i]);
    min_row = min(spreadsh[i]);
    
    checksum += max_row - min_row;
    
    
print checksum;