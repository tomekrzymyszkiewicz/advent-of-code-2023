with open('input.txt','r') as f:
    lines = f.readlines()
    
sum = 0
for line in lines:
    digits = [i for i in line if i.isdigit()]
    sum += int(''.join([digits[0],digits[-1]]))
    
print(sum)