# Q: What is the largest prime factor of the number 600851475143 ?
# takes 0.00022745132446289062 time

input = 600851475143

def largest_prime_factor(n):
    i = 2
    while(i*i < n/2):
        if n % i == 0:
            n //= i
        i += 2 if i > 2 else 1 # coz no prime no. is even
    return n

print(largest_prime_factor(input))