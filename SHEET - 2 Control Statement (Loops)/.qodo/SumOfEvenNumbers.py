A = int(input("Enter an integer A: "))
total = 0
for i in range(2, A + 1, 2):
    total += i
print("Sum of even numbers between 1 and", A, "is:", total)