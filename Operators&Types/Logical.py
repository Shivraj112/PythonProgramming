number1 = float(input())
number2 = float(input())

print(f"Are both numbers greater than 0? {number1 > 0 and number2 > 0}")
print(f"Is either number less than 0? {number1 < 0 or number2 < 0}")
print(f"Is it not true that both numbers are equal? {number1 != number2}")