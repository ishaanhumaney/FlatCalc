# Welcome to my First Python Based Calculator

print("--- DMAS Calc (Multiple Numbers) ---")
expr = input("Enter expression (use spaces between numbers and ops, e.g., 10 + 5 * 2): ")

# split into a list of strings
tokens = expr.split()

# Do not Forget Space between eacj Character

#       ADDITION AND SUBTRACTION 
i = 0
while i < len(tokens):
    if tokens[i] == '+' or tokens[i] == '-':
        op = tokens[i]
        num1 = float(tokens[i-1])
        num2 = float(tokens[i+1])
        
        if op == '+':
            val = num1 + num2
        else:
            val = num1 - num2
            
        tokens[i-1 : i+2] = [str(val)]
        i = 0
    else:
        i += 1

#      DIVISION AND MULTIPLICATION PASS
i = 0
while i < len(tokens):
    if tokens[i] == '/' or tokens[i] == '*':
        op = tokens[i]
        num1 = float(tokens[i-1])
        num2 = float(tokens[i+1])
        
        if op == '/':
            if num2 == 0:
                print("Error: division by zero")
                import sys; sys.exit()
            val = num1 / num2
        else:
            val = num1 * num2
            
        # replace the 3 tokens (num1, op, num2) with the result
        tokens[i-1 : i+2] = [str(val)]
        # reset index since list shrunk
        i = 0
    else:
        i += 1



print("Final Result:", tokens[0])