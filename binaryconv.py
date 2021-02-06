"""Decimal to binary conversion"""
value = int(input("Enter a number between 0...1023 (inclusive)"))
binary_string = ''
if 0 <= value < 1024:
    binary_string += str(value // 512)
    value %= 512

    binary_string += str(value // 256)
    value %= 256

    binary_string += str(value // 128)
    value %= 128

    binary_string += str(value // 64)
    value %= 64

    binary_string += str(value // 32)
    value %= 32

    binary_string += str(value // 16)
    value %= 16

    binary_string += str(value // 8)
    value %= 8

    binary_string += str(value // 4)
    value %= 4

    binary_string += str(value // 2)
    value %= 2

    binary_string += str(value)

    #print string
if binary_string != '':
    print(binary_string)
else:
    print("Oops! The number provided can't be converted!")