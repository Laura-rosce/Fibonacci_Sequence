print ('\n===== Welcome to Fibonacci Sequence ======\n')
number = int(input('How many numbers do you want to have in the sequence? '))
a,b = 0,1
while a < number:
    print (a, end = ' ')
    a, b = b, a+b
print ('\n')



        
    
