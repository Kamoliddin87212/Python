#1: is_prime(n) function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(4))

#2: digit_sum(k) function
def digit_sum(k):
    return sum(int(d) for d in str(k))

print(digit_sum(24))
print(digit_sum(502))

#3: Powers of two numbers
def powers_of_two(N):
    i = 1
    while i <= N:
        print(i, end=' ')
        i *= 2

powers_of_two(10)
