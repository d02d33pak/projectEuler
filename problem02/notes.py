# recursive method to print Fibonacci series upto Nth place
def fibb(n):
    if   n is 1 : return 1
    elif n is 2 : return 1
    else:
        return fibb(n-2) + fibb(n-1)

for i in range(1,10):
    print(fibb(i), end=' ')
print()
