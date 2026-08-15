# lab 1
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for number in numbers:
    squared_numbers.append(number**2)
print(squared_numbers)
print("\n")

comp_numbers = [number**2 for number in numbers]
print(comp_numbers)
print("\n")

# lab 2
prices = [10, 25, 40]

prices_with_vat = [round(price * 1.15, 2) for price in prices]
print(prices_with_vat)
print("\n")

# lab 3
names = ["SaRa", "ArEej", "MaJd", "AiL"]

lower = [name.lower() for name in names]
print(lower)
print("\n")

upper = [name.upper() for name in names]
print(upper)
print("\n")

titled = [name.title() for name in names]
print(titled)
print("\n")

# lab 4
c_temp = [20, 33, 15, 0]

f_temp = [(temp * 1.8 + 32) for temp in c_temp if temp > 0]

print(f_temp)
print("\n")

# lab 5
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []
for row in nested_list:
    for column in row:
        flattened_list.append(column)

    print(flattened_list)
    comp_flattened_list = [column for row in nested_list for column in row]
    print(comp_flattened_list)
    print("\n")


# lab 6
scores = [45, 55, 65, 86, 95]

passing_score = ["pass" if score >= 60 else "Failed" for score in scores]
print(passing_score)
print("\n")

# lab 7
skills = ["SQL", "PYTHON", "Git", "javascript", "git"]

skills_set = [skill.title() for skill in skills]
print(skills_set)
print("\n")

# lab 8
names1 = ["Sara", "Majd", "dala", "nouf"]
counted_char = [{"name": name, "count": len(name)} for name in names1]
print(counted_char)
print("\n")

# lab 9
new_names = ["Majd", "ail", "mada", "yamam"]

up = (name.upper() for name in new_names)

print(next(up))
print(next(up))
print(list(up))
print("-" * 5)
for x in up:
    print(x)
print("\n")
