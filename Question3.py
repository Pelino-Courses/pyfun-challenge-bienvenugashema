
# creating the function

def helper(*args, **kwargs):

    
    """
    This is a simple python calculator, you must insert numbers that are separeted by space and then 
    follow the action by choosing the action to perfom
    aactions:
            add ==> to add numbers
            multiply ==> to multiply numbers
            division ==> to divide numbers
            difference ==>  to find difference between numbers
    """

    numbers = [float(arg) for arg in args]

    if 'add' in kwargs:
        return sum(numbers)
    elif 'multiply' in kwargs:
        res = 1
        for num in numbers:
            res *= num
        return res
    elif 'division' in kwargs:
        res = numbers[0]
        for num in numbers[1:]:
            res /= num
        return res
    elif 'difference' in kwargs:
        res = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Division by zero is not allowed")
                continue
            res -= num
        return res
    else:
        return "Invalid operation"    


def calculate(numbers, operations):
    try:
        numbers = [float(x) for x in numbers.split()]

        if operations:
            return helper(*numbers, **{operations: True})
        return numbers
    except ValueError:
        return f"Error occured"
    # return arguments(*nums)
while True:
    try:
        num = input("Enter numbers separated by space: ")
        if num.lower() == 'quit':
            break
        action = input("Enter action (add/multiply/division/difference): ")
        res = calculate(num, action)
        print(f"Result: {res}")
    except KeyboardInterrupt:
        print(f"Exiting calculator")
        break