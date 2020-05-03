"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True: 
    user_input = input('your equation here >')
    token = user_input.split(" ")

    if "q" in token:
        print("you will exit")
        break

    operator = token[0] 
    num1 = float(token[1])
    num2 = float(token[2])

    result = None

    if operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == '*':
        result = multiply((num1),(num2))

    elif operator == '/':
        result = divide((num1), (num2))

    elif operator == 'square':
        result = square((num1))

    elif operator == 'cube':
        result = cube((num1))

    elif operator == 'pow':
        result = power((num1), (num2))

    elif operator == 'mod':
        result = mod((num1),(num2))

    print(result)



# Replace this with your code
