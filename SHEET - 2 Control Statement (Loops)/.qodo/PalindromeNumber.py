A = int(input("Enter an integer A: "))
original = abs(A)
reverse = 0
n = original

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

if reverse == original:
    print("Yes")
else:
    print("No")