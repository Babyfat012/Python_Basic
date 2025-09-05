import math


def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = int(input("Enter n: "))

    if check_prime(n):
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")

    sum = 0
    for i in range(1, n + 1):
        print(i, end=" ")
        sum += i
    print()
    print("Sum =", sum)

    print("Prime numbers from 1 to", n, ": ", end="")
    for i in range(1, n + 1):
        if check_prime(i):
            print(i, end=" ")
    print()

    print("First", n, "prime numbers: ", end="")
    prime = []
    num = 2
    while len(prime) < n:
        if check_prime(num):
            prime.append(num)
        num += 1
    print(prime)
