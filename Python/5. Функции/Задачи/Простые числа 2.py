def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())
count = 0
num = 2
while count < n:
    if is_prime(num):
        print(num, end = " ")
        count += 1
    num += 1