#Conditional expression
a = int(input("Enter a"))
b = int(input("Enter b"))
c = int(input("Enter c"))
d = int(input("Enter d"))
max = (a if (a>b and a>c and a>d) \
    else (b if ( b>c and b>d) \
        else (c if ( c>d) else d)))
print(max)