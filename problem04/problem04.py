# Q.  A palindromic number reads the same both ways. The largest palindrome made from the product of two 0-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def main():
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = str(i*j)
            if num == num[::-1]:
                if int(num) > max:
                    max = int(num)
    print(max)

if __name__ == '__main__':
    main()


