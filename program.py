# 4 types of data in python
# name = "string"
# integer = 20
# decimal = 25.5
# yes = True

# print(type(name))
# print(type(integer))
# print(type(decimal))
# print(type(yes))


# Ask for a name and return the hi name to user
name = input('Hi what is your name: ')
response = f"Hello, nice to meet you {name}"
print(response)

# price of mango to sell per kg
price_mango = 4
question = f"How many kilos of mango do you want {name}"
print(question)
kilo = float(input())
print(f"You want {kilo} Kg of mangoes")
total_price = price_mango*kilo
print(f"Your total price is £{total_price}")


# is the user male or female
gender = input(f"What is your gender {name}: ")
if gender == "male":
    print("Hi man")
elif gender == "woman":
    print("Hi woman")
else:
    print("Sorry we dont server LGBTQ")