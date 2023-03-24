lines = int(input())
count = 0
X = 0
while count < lines:
    count = count + 1    
    operation = str(input())
    if operation == 'X++' or operation == '++X':
        X = X + 1
    elif operation == 'X--' or operation == '--X':
        X = X - 1
print(X)
