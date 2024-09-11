#input: 5 & 1; output: 5.0
#input: 10 & y; output: Not the right type! Needs to be an integer.
#input: 23 & 0; output: Can't divide by zero!
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print(result)

main()