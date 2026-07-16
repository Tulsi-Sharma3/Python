# 1.
letter = "Hey i am {} and my country is {}"
name = "Tulsi"
country = "India"

print(letter.format(name,country))

# 2.
letter = "Hey i am {1} and my country is {0}"
name = "Tulsi"
country = "India"

print(letter.format(country,name))

# 3.
name = input("enter name : ")
country = input("enter coutry : ")
print(f" hey i am {name} and my country is {country}")
print(f" hey i am {{name}} and my country is {{country}}")

# 4.
dec = float(input("enter decimal values"))
print(f"decimal value will be : {dec}")

# 5.(upto 2 decimal places)
price = 33.333
txt = f"for my val {price: .2f}"
print(txt)