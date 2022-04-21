# Day 2 Task
'''Type the question as comment and execute the following
Q 1.Write a program that takes the length of an edge (an integer) as input and
prints the cube’s surface area as output.
'''
'''a=int(input("Enter the length of an edge"))
print("The surface area of 25cube is:",6*a**2)
# output-
Enter the length of an edge25
The surface area of cube is: 3750
'''
'''
Q 2. Write a Program to find the square root of a number by inputting the number
through key board.
'''
'''x=int(input("Enter the Number:"))
print("The square root of given number is:",x**0.5)
#output-
Enter the Number:16
The square root of given number is: 4.0
'''
'''
3. Write a program to find the area of a Rectangle by inputting the edge
through key board.
'''
'''h=int(input("Enter the Width(edge 1) of rectangle"))
b=int(input("Enter the length(edge 2) of rectangle "))
print("The Area of Rectangle is:",h*b)
#output-
Enter the Width(edge 1) of rectangle5
Enter the length(edge 2) of rectangle 4
The Area of Rectangle is: 20
'''
'''4.Write a program to swap the values of two variables using third variable by 
inputting the values of the variable through key board.
'''
'''v_1=25
v_2=30
v_3=v_1
v_1=v_2
v_2=v_3
print(v_1) #output - 30
print(v_2) #output - 25
'''
'''
Q 5. Write a program to swap the values of two variables without using third
variable by inputting the values of the variable through key board
'''
'''v_1=int(input("Enter 1st veriable:"))
v_2=int(input("Enter 2nd veriable:"))
print("Veriable 1 is:",v_2)
print("Veriable 2 is:",v_1)
# output -
Enter 1st veriable:25
Enter 2nd veriable:80
Veriable 1 is: 80
Veriable 2 is: 25
'''
'''
Q 6. Write a program to convert kilogram into pound. (1 kg = 2.20462 pound).
'''
'''
x=float(input("Enter the value in kg"))
print(x/0.453592,"lbs")
# output
Enter the value in kg1
2.2046244201837775 lbs
'''
'''
Q 7.Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area,
and volume.
'''
'''
r=float(input("Enter the Redius of Sphere"))
print("Diameter of Sphere is:",2*r)
print("Circumference of sphere is:",2*3.14*r)
print("Surface Area of Sphere is:",4*3.14*r**2)
output-
Enter the Redius of Sphere4.5
Diameter of Sphere is: 9.0
Circumference of sphere is: 28.26
Surface Area of Sphere is: 254.34
'''
'''
Q 8.An object’s momentum is its mass multiplied by its velocity. Write a program
that accepts an object’s mass (in kilograms) and velocity (in meters per
second) as inputs and then outputs its momentum.
'''
'''
m=float(input("Enter the mass of object in kilogram:"))
v=float(input("Enter the velocity of object in meter per second:"))
print("An object Momentum(p) is",m*v,"kg.m/s")
output-
Enter the mass of object in kilogram:30
Enter the velocity of object in meter per second:5.8
An object Momentum(p) is 174.0 kg.m/s
'''
'''
9.The kinetic energy of a moving object is given by the formula where m is the
object’s mass and v is its velocity. Modify the previous program you created
so that it prints the object’s kinetic energy as well as its momentum
'''
'''
m=float(input("Enter the mass of object in kilogram:"))
v=float(input("Enter the velocity of object in meter per second:"))
print("Momentum(p)of an object is",m*v,"kg.m/s")
print("The Kinetic Energy of an object",1/2*m*v**2,"jule")
#output-
Enter the mass of object in kilogram:3.5
Enter the velocity of object in meter per second:81
Momentum(p)of an object is 283.5 kg.m/s
The Kinetic Energy of an object 11481.75 jule
'''
'''
Q 10.Write a program that calculates and prints the number of minutes in a year.
'''
'''
y=365*24*60
print(y,"number of minute in a year")
output-
525600 number of minute in a year
'''
'''
Q 11.Light travels at 3 *108 meters per second. A light-year is the distance a light
beam travel in one year. Write a program that calculates and displays the
value of a light year.
'''
'''
speed_of_light=3*108 #in meter per second
time_in_ayear=365*24*60*60 # = 31,536,000 s.
Distance=speed_of_light*time_in_ayear #we know distance=speed  * time
print("value of a light year is:",Distance)
'''
'''
12.An employee’s total weekly pay equals the hourly wage multiplied by the total
number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that
takes as inputs the hourly wage, total regular hours, and total overtime hours
and displays an employee’s total weekly pay
'''
