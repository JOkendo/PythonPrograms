"""if statement, 
Python code that accepts a number and 
outputs it with leading zeros 
where necessary to achieve the 4 digits.
The program defaults any value less than 0 to 0
and value larger than 9999 to 9999"""

n = int(input("Enter a number: "))
if n < 0:
    n = 0
if n > 9999:
    n = 9999

#Determine the digit at various p.vs.
digit = n // 1000
print(digit, end="")
n %= 1000


digit = n // 100
print (digit, end = '')
n %= 100

digit = n // 10
print(digit, end='')
n %= 10

print(n, end='\n')