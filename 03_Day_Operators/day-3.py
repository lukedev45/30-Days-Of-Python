# # Arithmetic Operations in Python
# # Integers

# print('Addition: ', 1 + 2)
# print('Subtraction: ', 2 - 1)
# print('Multiplication: ', 2 * 3)
# print ('Division: ', 4 / 2)                         # Division in python gives floating number
# print('Division: ', 6 / 2)
# print('Division: ', 7 / 2)
# print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
# print('Modulus: ', 3 % 2)                           # Gives the remainder
# print ('Division without the remainder: ', 7 // 3)
# print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# # Floating numbers
# print('Floating Number,PI', 3.14)
# print('Floating Number, gravity', 9.81)

# # Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# # Declaring the variable at the top first

# a = 3 # a is a variable name and 3 is an integer data type
# b = 2 # b is a variable name and 3 is an integer data type

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# # I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
# print(total) # if you don't label your print with some string, you never know from where is  the result is coming
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# # Declaring values and organizing them together
# num_one = 3
# num_two = 4

# # Arithmetic operations
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_two
# remainder = num_two % num_one

# # Printing values with label
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)


# # Calculating area of a circle
# radius = 10                                 # radius of a circle
# area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')

# print(3 > 2)     # True, because 3 is greater than 2
# print(3 >= 2)    # True, because 3 is greater than 2
# print(3 < 2)     # False,  because 3 is greater than 2
# print(2 < 3)     # True, because 2 is less than 3
# print(2 <= 3)    # True, because 2 is less than 3
# print(3 == 2)    # False, because 3 is not equal to 2
# print(3 != 2)    # True, because 3 is not equal to 2
# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False

# # Boolean comparison
# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)
# print('True and True: ', True and True)
# print('True or False:', True or False)

# # Another way comparison 
# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# print(3 > 2 and 4 > 3) # True - because both statements are true
# print(3 > 2 and 4 < 3) # False - because the second statement is false
# print(3 < 2 and 4 < 3) # False - because both statements are false
# print(3 > 2 or 4 > 3)  # True - because both statements are true
# print(3 > 2 or 4 < 3)  # True - because one of the statement is true
# print(3 < 2 or 4 < 3)  # False - because both statements are false
# print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
# print(not True)      # False - Negation, the not operator turns true to false
# print(not False)     # True
# print(not not True)  # True
# print(not not False) # False

## Exercises

# age = 22
# height = 1.70
# complex_number = 3 + 2j

# def tri_area():
#     base = float(input("What is the base of the triangle you wish to calculate?\n"))
#     height = float(input("What is the height of the triangle?\n"))
#     return 0.5 * base * height  

# print(tri_area())

# def tri_perm():
#     a = float(input("What is the length of side a?\n"))
#     b = float(input("What is the length of side b?\n"))
#     c = float(input("What is the length of side c?\n"))
#     return a + b + c

# print(tri_perm())

# def rect_perm():
#     length = float(input("What is the length of the rectangle?\n"))
#     width = float(input("What is the width of the rectangle?\n"))
#     area = length * width
#     return area

# print(rect_perm())

# def cir_area_circ():
#     pi = 3.14
#     radius = float(input("What is the radius of the circle?\n"))
#     area =  pi * (radius**2)
#     circum = 2 * pi * radius
#     return area, circum

# print(cir_area_circ())

# def linear():
#     # For the line y = 2x - 2
#     slope = 2
#     y_intercept = (0, -2)
#     x_intercept = (1, 0)
#     return slope, x_intercept, y_intercept

# print(linear())

# def linear_dist(x1,x2,y1,y2):
#     slope = (y2-y1)/(x2-x1)
#     distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
#     return slope, distance

# print(linear_dist(2,6,2,10))

# slope1, y_int, x_int = linear()
# slope2, dist = linear_dist(2, 6, 2, 10)

# if slope1 == slope2:
#     print(f"The slopes are equal: {slope1}")
# elif slope1 > slope2:
#     print(f"Slope from linear ({slope1}) is greater than slope from linear_dist ({slope2})")
# else:
#     print(f"Slope from linear ({slope1}) is less than slope from linear_dist ({slope2})")

# def quad_solver(a,b,c):
#     y1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
#     y2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
#     if y1 == y2:
#         return f"We have a repeated root of {y1}."
#     elif y1 != y2:
#         return y1,y2
#     else:
#         return "There are no real solutions."

# print(quad_solver(1,6,9)) # Repeated root
# print(quad_solver(1,0,1)) # Imaginary roots
# print(quad_solver(1,6,-12)) # Repeated root

# print(len("python") > len("dragon"))

# if "on" in "python" and "dragon":
#     print(True)
# else:
#     print(False)

# if "jargon" in "I hope this course is not full of jargon.":
#     print("True")
# else:
#     print("False")
# print("There is no 'on' in python and dragon", 'on' in 'python' and 'dragon')
# print("There is no 'on' in python and dragon", 'on' not in 'python' and 'dragon')

# print("There is no 'on' in python and dragon", ('on' in 'python') and ('on' in 'dragon'))
# print("There is no 'on' in python and dragon", ('on' not in 'python') and ('on' not in 'dragon'))

# print(str(float(len("python"))))
# print(type((str(float(len("python"))))))

# def even_check(x:int):
#     if x % 2 == 0:
#         return print(f"{x} is even.")
#     else:
#         return print(f"{x} is odd.")

# even_check(21)
# even_check(12)

# if 7 // 3 == int(2.7):
#     print("yes")
# else:
#     print("no")

# if int('9.8') == type(10):
#     print('True')
# else:
#     print('False')

# def wage_cal():
#     hours = float(input("Number of hours: \n"))
#     rate = float(input("Going rate per hour: \n"))
#     weekly = hours * rate
#     return print(f"Your weekly earning is {weekly}.")

# wage_cal()

# def square_table():
#     for i in range(1, 6):
#         print(i, i**0, i**1, i**2, i**3)
    
# square_table()
