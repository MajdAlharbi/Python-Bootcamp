user = int(input("Enter the maximum number:"))
count = 0
total = 0
for number in range(1, user + 1):
    total += number
    if number % 2 == 0:
        count += 1
        print(f"Even numbers: {number}")
    else:
        print(f"odd number: {number}")

print(total)
print(f"number of even numbers {count}")
