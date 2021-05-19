def calculator():
    operation = []
    
    while True:
        operand = input(': ')
        if operand == '=':
            break
        operation.append(operand)
        result = int(operation[0])
    for i in range(0, len(operation)):
        if operation[i+1] == '+':
            result += int(operation[i+2])
        if operation[i+1] == '-':
            result -= int(operation[i+2])
        if operation[i+1] == '*':
            result *= int(operation[i+2])
        if operation[i+1] == '/':
            result /= int(operation[i+2])
        if i+3 < len(operation):
            i+=3
        else:
            return result
print(calculator())