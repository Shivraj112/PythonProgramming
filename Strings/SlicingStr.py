# Slicing helps to extract part of string , such as word,phrase, 
# rather than a single character like Accessing String through index

phrase = "Hello, Python!"
print(phrase[0:5])
print(phrase[7:13])
print(phrase[:5])
print(phrase[7:])


date = '2024-10-16'
year = date[0:4]
month = date[5:7]
day = date[8:10]

print("Year:",year)
print("Month:",month)
print("Day:",day)