'''
Code to check whether a number is prime or not
'''
def check_one():
    '''To check whether prime or not'''
    num = int(input("Enter Number to check - "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
