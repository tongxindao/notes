def print_prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print("%d is a prime number" % i)


print_prime(6)
