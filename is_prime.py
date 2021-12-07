def is_prime(n):
    if n == 1 or n ==0:
        return False
    if n == 2 or n == 3:
        return True
    i = 2
    while i * i <= n:
        if n % i ==0:
            return False
        i += 1
    return True


n = int(input())

print(is_prime(n))