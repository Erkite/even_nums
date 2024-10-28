number = input("Enter a number: ")
for digit in number:
    if digit.isdigit() and int(digit) % 2 == 0:
        print(digit)