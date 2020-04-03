# Q: Find the sum of all the multiples of 3 or 5 below 1000.

# method 01 takes 0.00018180100050813053 time 
multiples = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        # summ += i
       multiples.append(i) 

print(sum(multiples))


# method 02 takes 0.0003612910004449077 time
# summ = 0
# for i in range (1, 1000):
#     if i % 3 == 0 or i % 5 == 0:
#         # summ += i
#        multiples.append(i) 

# print(summ)
