n = 15
isprime = True

if n < 2:
    isprime = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            isprime = False
            break

if isprime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
