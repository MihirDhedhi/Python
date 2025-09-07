length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)





num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")





side = float(input("Enter side of cube: "))

area = 6 * (side ** 2)
volume = side ** 3

print("Surface Area of Cube:", area)
print("Volume of Cube:", volume)






x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

z = (x + y) * (x - y)

print("The value of z is:", z)





x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

# The equation simplifies to (x + y)^2 - 2xy = x^2 + y^2
z = (x + y) * (x + y) - 2 * x * y

print("The value of z is:", z)




celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
