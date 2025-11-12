# 'Day 2: 30 Days of Python'

first_name = 'Luke'
surname = 'Devlin'
country = 'Ireland'
city = 'Cookstown'
age = 22
year =2025
is_married = False
is_true = True
is_light_on = False
laptop , os = 'Asus', 'Omarchy'

print(type(first_name))
print(type(surname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(laptop))
print(type(os))

print(len(first_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_two*num_one
divsion=num_one/num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

def details():
    first = input("What is your first name?")
    last = input("What is your last name?")
    country = input("Where are you from?")
    age = input("What age are you?")
    return [first,last,country,age]

answer = input("Can I take your details [Y/n]?")
if answer == "":
    details()
elif answer == "n":
    pass
