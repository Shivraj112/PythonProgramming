# Type Casting - it convert the string into type you need
# i.e number or boolean

# Taking integer input

temperature = int(input("Enter today's temperature in degrees: "))
print("Today's temperature is: ", temperature,"degrees")

# Taking float input

height = float(input("Enter your height in meters: "))
print("Your height is: ", height, "meters")

# Taking Boolean input

user_response = input("Do you like ice cream? (yes/no): ").lower()
is_ice_cream_lover = user_response == "yes"
print("Do you like ice cream?", is_ice_cream_lover)