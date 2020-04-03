# to check if a number is prime or not
# use x**0.5 instead of math.sqrt(x)
def is_prime(n):
    for i in range(int(n**0.5), 1, -1):
    # using the same for 'i' in main solution
    # since i will always be a prime number (finding prime factors)
    # i*i should always be less than 'n'
        if n % i == 0:
            return False 
    return True


# a function to find factors of a number
def factors(n):
    for i in range(n//2, 1, -1):
        if n % i == 0:
            print(i)

print(is_prime(67))
factors(100)

# NOTES:
# for example 100
# has 9 factors : 1,2,4,5,10,20,25,50,100
# has 7 proper factors : exclude 1 and 100,
#       therefore : 2,4,5,10,20,25,50
# has only 2 prime factors [prime factorization]
# 2 and 5 [2 x 2 x 5 x 5]
# unique prime factors are 2 and 5
# 