'''Recursive factorial'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print(factorial(10))
main()