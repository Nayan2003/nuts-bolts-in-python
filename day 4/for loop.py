#Q1) print  all natural numbers from 1 to n
'''n=int(input("Enter the number : "))
for x in range(1,n+1):
    print(x)
output=
Enter the number : 25
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
'''
#Q2)print allnatural numbers in reverse (frpm n to 1)
'''n=int(input("Enter the number :"))
for x in range(n,0,-1):
    print(x)
output-
Enter the number :25
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
#Q3)print all  even numbers between 1 to n
'''n=int(input("Enter the number :"))
for x in range(0,n+1,2):
    print(x)
output-
Enter the number :25
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
'''
#Q4)print all odd number between 1 to n.
'''n=int(input("Enter the number :"))
for x in range (1,n+2,2):
    print(x)
output-
Enter the number :25
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
'''
#Q5)find sum of all natural numbers between 1 to n
'''n=int(input("Enter the number:"))
sum=0
for i in range(n+1):
    sum+=i
print("the sum of",n,"natural number is:",sum)
output-
Enter the number:5
the sum of 5 natural number is: 15
'''
#Q6)find sum of all even numbers between 1 to n
'''n=int(input("Enter the number:"))
sum=0
for i in range(0,n+1,2):
    sum+=i
print("the sum of",n,"even number is:",sum)
output-
Enter the number:8
the sum of 8 even number is: 20
'''
#Q7)find sum of all odd numbers between 1 to n
'''n=int(input("Enter the number :"))
sum=0
for i in range(1,n+2,2):
    sum+=i
print("the sum of",n,"even number is:",sum)
'''
#Q8)print multiplication table of any number.
'''n=int(input("Enter any number:"))
sum=0
for i in range(1,11):
    print(n,"x",i,"=",n*i)
output-
Enter any number:8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
'''
#Q9)calculate factorial of a number.
'''n=int(input("Enter the number "))
fac=1
for i in range (1,n+1):
        fac*=i
print("factorial of",n,"is",fac)
output-
Enter the number 5
factorial of 5 is 120
'''
#10) Enter a word and print reverse of it.
'''w=input("enter the word")
n=len(w)
for i in range(n-1,-1,-1):
    print(w[i])
output-
enter the wordnayan
n
a
y
a
n
'''
#11. Enter a number and print its reverse.
'''num=str(input("Enter the number"))
n=len(num)
for i in range(n-1,-1,-1):
    print(num[i])
output-
Enter the number70485262273
3
7
2
2
6
2
5
8
4
0
7
'''
#12. Write a program to print all multiple of 5 with in n.
'''n=int(input("Enter the number :"))
for x in range(5,n+1):
    if x%5==0:
        print("this all numbers divisible by 5",x)
output-
Enter the number :54
this all numbers divisible by 5 5
this all numbers divisible by 5 10
this all numbers divisible by 5 15
this all numbers divisible by 5 20
this all numbers divisible by 5 25
this all numbers divisible by 5 30
this all numbers divisible by 5 35
this all numbers divisible by 5 40
this all numbers divisible by 5 45
this all numbers divisible by 5 50
'''
#13. Input a number and check whether it is prime or not.
'''
n=int(input("Enter the number :"))
x=True
for i in range(2,n):
    if n%i==0:
        x=False
        break
if x==True:
    print("this number is prime number")
else:
    print("This is not prime number:")

output-
Enter the number :5
this number is prime number
'''
