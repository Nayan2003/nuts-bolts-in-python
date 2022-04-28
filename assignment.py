#Try this 1


#1. Get the output of the following string with the use of Single Quotes: Welcome to the Python World
'''print('Welcome to the Python World')
output-
Welcome to the Python World
'''
#2. Get the output of the following string with the use of Double Quotes: I'm a Python learner
'''print("I'm a Python learner")
output-
I'm a Python learner
'''
#3. Get the output of the following string with the use of Triple Quotes: I'm a Python learner and I live in a world of "Python"
'''
print('I'm a Python learner and I live in a world of "Python"')
output-
I'm a Python learner and I live in a world of "Python"
'''
#4. Create a multiline String:
''' Python 
 For 
 Better 
 Life
 '''
'''str_1="Python"
str_2="for"
str_3="better"
str_4="life"
print(str_1)
print(str_2)
print(str_3)
print(str_4)
output-
Python
for
better
life
'''





#Try this 2


#1. Assign your name, mobile number and address in three different variables with a comment ‘My contacts’.
#My contact
'''
name="nayan"
mo_no="7045262273"
address="panvel maharastra"
print(name)
print(mo_no)
print(address)
output-
nayan
7045262273
panvel maharastra
'''
#2. Assign the value of the radius of a circle in a variable ‘r’. Calculate and store the values of its circumference and area in two different variables.
'''r=35
cicumference=2*3.14*r
area=3.14*r**2
print("The circumfarence of circle is:",cicumference)
print("The area of circle is",area)
output-
The circumfarence of circle is: 219.8
The area of circle is 3846.5
'''
#3. Assign three numbers in the variables x, y and z. Calculate and store the mean of them in a suitable variable.
'''x=35
y=20
z=4
mean=(x+y+z)/3
print("Mean of three veriable is:",mean)
output-
Mean of three veriable is: 19.666666666666668
'''
#4. Assign hour. Covert this into minutes and seconds.
'''houre=24
min=houre*60
sec=min*60
print(houre)
print(min)
print(sec)
output-
24
1440
86400
'''
#5. Assign the value of temperature in Celsius. Convert this into Fahrenheit using the formula c*9./5+32=f
'''print("convert temprature - celsius into faharenheit")
c=45
form=(c*9/5)+32
print(c,"degree celsius converted into",form,"fahrenheit")
output-
convert temprature - celsius into faharenheit
45 degree celsius converted into 113.0 fahrenheit
'''


#Try this 3


'''
Q1. Assign the strings ‘He is ‘ in the variable x, ‘telling truth.’ in y and ‘telling lie.’ 
in z.
Concatenate them into two sentences.
Display ‘telling truth’ thrice.
Display first two letters of x,y and z.
Display alternate letters of ‘telling’.
'''
'''x='He is'
y='telling truth'
z='telling lie'
#Concatenate them into two sentences.
print(x+y)
print(x+z)
#Display ‘telling truth’ thrice.
print(y*3)
#Display first two letters of x,y and z.
print(x[0:2])
print(y[0:2])
print(z[0:2])
#Display alternate letters of ‘telling’.
print(y[0:7:2])
'''
'''
Q2. Assign and display a string ‘We are Khalsite.’
Display all in small letter.
Display all in capital letter.
Find the index of ‘r’ in the string.
Replace ‘We’ by ‘You’.
Count how many ‘e’ is there.
What’s the total length of the string.
Display all alternate characters from the starting of the string
'''
'''
k='We are Khalsite'
#Display all in small letter.
print(k.lower())  #we are khalsite
#Display all in capital letter.
print(k.upper())  #WE ARE KHALSITE
#Find the index of ‘r’ in the string
print(k.find('r')) #4
#Replace ‘We’ by ‘You’
print(k.replace('We','You')) #You are Khalsite
#Count how many ‘e’ is there.
print(k.count('e')) #3
#What’s the total length of the string
print(len(k)) #15
#Display all alternate characters from the starting of the string.
print(k[0:15:2]) #W r hlie
'''




'''Q3. Create two lists containing numbers and strings. Concatenate them into a third 
string. Change the 3rd element of the third string. Display the sub list 
containing 3rd, 4th and 5th element from the last updated string.
'''
'''l_1=['arpita','anjali','shalu','shrutika','rinaz','pranay']
l_2=[301,302,303,304,305,306]
'''             #asking doubt




#Try this 4
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



#Try This Using while loop 5

#1.Print all natural numbers from 1 to n
'''n=int(input("Enter the number"))
i=1
while i<=n:
    print(i)
    i+=1
#output-
Enter the number55
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
'''
'''n=int(input("Enter the number"))
#Q 2 print all natural numbers in revers (from n to 1)
i=1
while i<=n:
    print(n)
    n-=1
#output-
Enter the number50
50
49
48
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
'''
'''#Q3print all even numbers from 1 to 100.
n=0
while n<=100:
    print(n)
    n+=2
#output-
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
97
98
99
100
'''
'''#Q 4 print all odd number between 1 to 100
n=1
while n<=100:
    print(n)
    n+=2
#output-
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
'''
'''#Q 5 find sum of all natural numbers between 1 to n.
n=int(input("enter the number"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=1 
print(sum)
#output-
enter the number6
21
'''
'''#Q 6 find sum of all even numbers between 1 to n'''
'''n=int(input("enter the number"))
i=2
sum=0
while i<=n:
    sum+=i
    i+=2
print(sum)
output-
enter the number10
30
'''
'''#Q.7 find sum of all odd number between 1 to n.'''
'''n=int(input("Enter the number"))
i=1
sum=0
while i<=n:
    sum+=i
    i+=2
print(sum)
'''
#Q.8 print any multiplication table
'''n=2
i=1
while i<=10:
    print(n,'*',i,"=",i*n)
    i+=1
#output
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
2 * 10 = 20
'''
#Q9. Calculate sum of digits of a number.
'''n=int(input("Enter a number"))
total=0
while (n>0):
    dig=n%10
    total+=dig
    n=n//10
print("The total sum of digits is:",total)
output-
Enter a number212
'''
#10. Calculate product of digits of a number.
'''n=int(input("Enter a number :"))
total=1
while (n>0):
    dig=n%10
    total*=dig
    n=n//10
print("The total product of digits is",total)
output-
Enter a number :42
The total product of digits is 8
'''
#11. Enter a number and print its reverse.
'''
n=input("Enter a number ")
rev= n[::-1]
print(rev)
output-
Enter a number 32110
01123
'''


#Try This Using for loop 6

'''# Q.1: Print all natural numbers from 1 to n
n=int(input('Enter a natural number'))
for x in range(1,n+1,1):
    print(x)

***** # OUTPUT # *****
Enter a natural number12
1
2
3
4
5
6
7
8
9
10
11
12

# Q.2: Print all natural numbers in reverse (from 1 to n)
n=int(input('Enter a natural number'))
for x in range(n,0,-1):
    print(x)

***** # OUTPUT # *****
Enter a natural number12
12
11
10
9
8
7
6
5
4
3
2
1

# Q.3: Print all even numbers between 1 to n
n=int(input('Enter an even number'))
for x in range(0,n+1,2):
    print(x)

***** # OUTPUT # *****
Enter an even number13
0
2
4
6
8
10
12

# Q.4: Print all odd numbers between 1 to n
n=int(input('Enter an odd number'))
for x in range(1,n+1,2):
    print(x)

***** # OUTPUT # *****
Enter an odd number15
1
3
5
7
9
11
13
15

# Q.5: Find sum of all natural numbers between 1 to n
n=int(input('Enter a natural number'))
sum=0
for x in range(n+1):
    sum=sum+x
print('the sum of 1st',n,'natural is ',sum)

***** # OUTPUT # *****
Enter a natural number5
the sum of 1st 5 natural is  15

# Q.6: Find sum of all even numbers between 1 to n
n=int(input('Enter a number'))
sum=0
for x in range(0,n+1,2):
    sum=sum+x
print('the sum of 1st',n,'even is ',sum)

***** # OUTPUT # *****
Enter a number13
the sum of 1st 13 even is  42

# Q.7: Find sum of all odd numbers between 1 to n
n=int(input('Enter a number'))
sum=0
for x in range(1,n+1,2):
    sum=sum+x
print('the sum of 1st',n,'odd is ',sum)

***** # OUTPUT # *****
Enter a number13
the sum of 1st 13 odd is  49

# Q.8: Print multiplication table for any number
n=int(input('Enter a number'))
for x in range(1,11):
    print(n,"x",x,"=",n*x)

***** # OUTPUT # *****
Enter a number13
13 x 1 = 13
13 x 2 = 26
13 x 3 = 39
13 x 4 = 52
13 x 5 = 65
13 x 6 = 78
13 x 7 = 91
13 x 8 = 104
13 x 9 = 117
13 x 10 = 130

# Q.9: Calculate factorial of a number.
n=int(input('Enter a number'))
fac=1
for x in range(1,n+1):
    fac*=x
print("factorial of",n,"=",fac)

***** # OUTPUT # *****
Enter a number5
factorial of 5 = 120

# Q.10: Enter a word and print reverse of it
n=str(input('Enter word:'))
a=len(n)
for x in range(a-1,-1,-1):
    print(n[x])

***** # OUTPUT # *****
Enter word:python
n
o
h
t
y
p

# Q.11: Enter a number and print it's reverse
n=str(input('Enter number:'))
a=len(n)
for x in range(a-1,-1,-1):
    print(n[x])

***** # OUTPUT # *****
Enter number:8931007649
9
4
6
7
0
0
1
3
9
8

# Q.12: Write a program to print all multiple of 5 within n.
n=int(input('Enter number:'))
for x in range(5,n+1):
    if x%5==0:
       print(x)

***** # OUTPUT # *****    
Enter number:35
5
10
15
20
25
30
35

# Q.13: Input a number and check whether it is prime or not
n=int(input('Enter number:'))
r=0
for x in range(1,n+1):
    if n%x==0:
        r+=1
if r==2:
    print(n,"is a prime number",end=".")
else:
    print(n,"is not a prime number",end=".")

***** # OUTPUT # *****
Enter number:23
23 is a prime number.

Enter number:45
45 is not a prime number.'''

# Q.13: Input a number and check whether it is prime or not
'''n=int(input('Enter number:'))
x=True
for i in range(2,n):
    if n%i==0:
        x = False
        break
if x==True:
    print(n,"is prime number")
else:
    print(n,"is not prime number")

#output
Enter number:5
5 is prime number
'''

#Q14. Write a program to print the following pattern using a loop.
'''for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*", end='')
        else:
            print(" ",end='')
    print()
output-
*   
**  
*** 
****
'''


#15. Find all prime number between 1 to n
'''
n= int(input("Find prime numbers upto : "))

print("\nAll prime numbers upto",n, "are : ")

for num in range(2, n + 1):

    i = 2

    for i in range(2, num):
        if(num % i == 0):
            i = num
            break;

    # If the number is prime then print it.
    if(i != num):
        print(num, end=" ")
        
output-
All prime numbers upto 80 are : 
3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 
'''