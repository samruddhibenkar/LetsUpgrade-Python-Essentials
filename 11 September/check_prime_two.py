def check_two(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                return "not prime"
                break
        else:
            return "prime"
