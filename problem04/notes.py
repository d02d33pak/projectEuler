# first solution [brute force]
# takes 0.4604487419128418 time
# improved time 0.3379378318786621

def is_palindrome(n):
    ''' removed the function later on as it could be done in one line in main itself'''
    ''' improves time, takes 0.27950096130371094'''
    # rev = str(n)
    # rev = rev[::-1]
    # rev = int(rev)
    # above statements can be done in one line
    # rev = int(str(n)[::-1])
    # if n == rev:

    if n == n[::-1]:    # if n is already string
        return True
    return False

def main():
    max = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            # num = i*j
            # changing this improves time
            num = str(i*j)
            if is_palindrome(num):
                # if num > max:
                if int(num) > max:
                    # max = num
                    max = int(num)
    print(max)

if __name__ == '__main__':
    main()
