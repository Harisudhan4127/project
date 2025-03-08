option = int(input('1. Table\n2. Cube\n3. Fibonacci\n4. Factorial\n5. Close\n'))

if option == 1:
    print('Tables')
    j = int(input('Enter the table name : '))
    i = int(input('Enter the table limit : '))
    for i in range(1, i+1 , 1):
        print(i,'X', j, '=', i*j)


elif option == 2:
    print('Cube')
    num = int(input('Enter a number: '))
    print(f'Cube of {num} is {num**3}')
elif option == 3:
    print('Fibonacc')
    n = int (input('Enter the number of terms : '))
    a = 0
    b =  1
    next_term = 0
    for i in range(0, n, 1):
        a = b
        b = next_term
        next_term = a+b
    print(next_term)
elif option == 4:
    print('Factorial')
    num = int(input('Enter a number: '))
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print(f'Factorial of {num} is {fact}')
else:
    print('closed')