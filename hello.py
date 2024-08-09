def factorial (n):
    if n == 0:
        return 1
    else: 
        return n * factorial (n - 1)
    
number = 5
result = factorial(number)
print(f"O fatorial de {number} is {result}.")