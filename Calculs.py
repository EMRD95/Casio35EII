#Define the function
def calculator(x, y, operator):
    if operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    elif operator == '+':
        return x + y
    else:
        return "Invalid operator"

#Call the function
calculator(10, 5, '+')
