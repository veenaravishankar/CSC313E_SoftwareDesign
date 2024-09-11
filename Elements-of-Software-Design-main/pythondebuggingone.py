#expected output:
#Is a multiple of 4!
#Is not a multiple of 4 :(

def main():
    digits = [4, 5, 21, 10, 25, 6]
    product = multiply(digits)

    if(is_a_multiple_of_4):
        print("Is a multiple of 4!")
    else:
         print("Is not a multiple of 4 :(")
    

    new_digits = [3, 3, 5, 25]
    product = multiply(new_digits)

    if(is_a_multiple_of_4):
        print("Is a multiple of 4!")
    else:
         print("Is not a multiple of 4 :(")


def multiply(list):
    total = 0
    for number in list:
        total *= number

    return total


def is_a_multiple_of_4(num):
    if(num // 4 == 0):
        return True
    
    return False

main()
#expected output:
#Is a multiple of 4!
#Is not a multiple of 4 :(
