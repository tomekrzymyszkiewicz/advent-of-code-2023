import re
with open('input.txt','r') as f:
    lines = f.readlines()
    
numbers = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}
    
sum = 0
for line in lines:
    digits = []
    for i in range(len(line)):
        for j in range(i + 1, i + max(map(len,numbers.keys())) + 1):
            char = line[i:j]
            if char.isdigit():
                digits.append(char)
            if char in numbers.keys():
                digits.append(numbers[char])
    sum += int(''.join([str(digits[0]),str(digits[-1])]))
    
print(sum)