expression = input().split('-')
result = 0

for i in map(int,expression[0].split('+')):
    result += i

for i in expression[1:]: 
    result -= sum(map(int,i.split('+')))

print(result)
