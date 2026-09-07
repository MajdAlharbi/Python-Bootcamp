student_name = input("student name: ")
score = int(input("score:"))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"

else:
    grade = "Needs improvements"

print("Student", student_name)
print("score", score)

print("grade:", grade)

# ---------------------------

items = ["coffee", "sandwich", "juise"]
prises = [10, 20, 30]
total = 0
for prise in prises:
    total += prise

vat = total * 0.15
final_total = total + vat

print("items:", items)
for item in items:
    print("-", item)

print("Total:", total)
print("VAT:", vat)
print("Final Total:", final_total)
