# Float is a number has decimal point

price = 19.99
weight = 65.5

length = 7.5
width = 3.2

area = length * width
permiter = 2 * (length + width)
print("The area of the rectangle with length 7.5 and width 3.2 is:",area)
print("The perimeter of the rectangle with length 7.5 and width 3.2 is:",permiter)


price1 = 49.99
price2 = 79.50
price3 = 120.75

total_price = price1 + price2 + price3
average_price = total_price / 3

print(f"The total price of the items is: {total_price:.2f}")
print(f"The average price of the items is: {average_price:.2f}")


celsius = 36.6
fahrenheit = (celsius * 9/5) + 32

print(f"The temperature {celsius:.1f} deg C is equivalent to {fahrenheit:.2f} deg F")