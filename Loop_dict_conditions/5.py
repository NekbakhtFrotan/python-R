n = int(input("Enter a number greater than 1: "))
is_prime = True
for i in range(2,n):
    if n % i == 0:
        is_prime = False
        print(f"{n} is not prime. its divisor is {i}")
if is_prime:
    print(f"{n} is a prime number")