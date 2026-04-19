import art
print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    first_number = float(input("What's the first number?: "))

    is_continue = 1
    while is_continue:
        print("+\n-\n*\n/")
        operation_type = input("Pick an operation: ")
        last_number = float(input("What's the next number?: "))

        output = operations[operation_type](first_number, last_number)
        print(f"{first_number} {operation_type} {last_number} =  {output}")
        want_continue = input(
            f"Type 'y' to continue calculating with {output}, or type 'n' to start a new calculation: ")
        if want_continue == "n":
            is_continue = False
        elif want_continue == "y":
            first_number = output

#print(operations["*"](4,8))
