# .split() method helps to split into list of words

text = "Apple,banana,cherry"
fruits = text.split()
print(fruits)

supreme = "Shiva, Bhairava, Mahakal"
god = supreme.split()
print(god) 


full_name = "John Michael Doe"
name_parts = full_name.split()

initials_name = f"{name_parts[0]} {name_parts[1][0]}. {name_parts[2][0]}."

print("Name parts:",name_parts)
print("Formatted name with initials:",initials_name)