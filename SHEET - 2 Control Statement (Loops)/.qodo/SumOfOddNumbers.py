A = int(input("Enter an integer A: "))
total = 0
for i in range(1, A + 1, 2):
    total += i
print("Sum of odd numbers between 1 and", A, "is:", total)