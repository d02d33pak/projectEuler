# Q: Consider the terms in the Fibonacci sequence whose values < four million,
#    find the sum of the even-valued terms.

# a little easy to understand

# a, b, c, total = 1, 1, 0, 0
# while (c < 4000000):
#     c =  a + b
#     if c % 2 == 0:
#         total += c
#     a, b = b , c


# same but little more efficient

a, b, total = 1, 1, 0
while(a < 4000000):
    if a % 2 == 0:
        total += a
    a,b = b,a+b

print(total)

