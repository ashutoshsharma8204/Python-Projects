N = int(input("Enter an integer N: "))
count = 0
n = abs(N)  # Handle negative numbers
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1
print("Number of digits:", count)