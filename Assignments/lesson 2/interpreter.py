def main():
    # Prompt the user for input
    expression = input("Expression: ")

    # Split input into components
    x, operator, z = expression.split()

    # Convert x and z to integers
    x = int(x)
    z = int(z)

    # Perform the operation
    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z
    else:
        print("Invalid operator")
        return

    # Print the result formatted to one decimal place
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()
#OR

que=input("Expression: ")
x,y,z= que.split()
x= int(x)
z=int(z)

if y=="+":
    result= x+z
elif y=="-":
    result=x-z
elif y=="*":
    result=x*z
elif y=="/":
    result=x/z
print(f"{result:.1f}")
