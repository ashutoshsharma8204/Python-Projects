N = int(input("Enter an integer N: "))
total = 0
n = abs(N)  # Handle negative numbers
while n > 0:
    digit = n % 10
    total += digit
    n //= 10
print("Sum of digits:", total)