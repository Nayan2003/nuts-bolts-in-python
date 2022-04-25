#Q2 find max num between 3 num
'''x=int(input("Enter 1 st num"))
y=int(input("Enter 2nd st num"))
z=int(input("Enter 3rd num"))
if x>y and x>z:
    print("first num is maximum")
elif y>x and y>z:
    print("second num is maximum")
elif z>x and z>y:
    print("Third number is maximum")
    
output-
Enter 1 st num1
Enter 2nd st num5
Enter 3rd num9
Third number is maximum
'''
#Q3 chack whether number is negative, positive, zero
'''x=int(input("Enter the number:"))
if x>0:
    print("Number is positive")
elif x<0:
    print("Number is negative")
elif x==0:\
     print("Number is zero")
#output-

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number:55
Number is positive

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number:-78
Number is negative

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number:0
Number is zero
'''
#Q4 check whether number is divisible by 5 and 11 or not
'''x=int(input("Enter the number:"))
if x%5==0:
    print("Given number is divisible by 5")
elif x%11==0:
    print("Given number is divisible by 11")
else:
    print("Given number is naither divisible by 5 nor 11")
output-
================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number:55
Given number is divisible by 5

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number:77
Given number is divisible by 11
'''
#Q5 chack whether a number is even or odd
    
'''x=int(input("Enter the number?:"))
if x%2==0:
    print("Given number is even.....")
else:
    print("Given number is odd")
#output-
================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number?:8
Given number is even.....

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number?:3
Given number is odd

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter the number?:88
Given number is even.....
'''
#Q6 chack whether year is leap year or not
'''year=int(input("Enter Year"))
if year%4==0:
    print(year,"this is leap year")
else:
    print(year,"this is not leap year")

output-
Enter Year2256
2256 this is leap year
'''
#Q7 chack whether charecter is alfabet or not
'''x=(input("Enter a charecter"))
print("ASCII of ",x,"is",ord(x))

if 90>=ord(x)>=65 or 97<=ord(x)<=122:
    print("Given charecter is alfabet")
else:
    print("Given charechter is not alfabet")
output-
================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter a charecterj
Given charecter is alfabet
'''
#Q8 input any alfabet and chack whethr is vowel or not.
'''x=input("Enter charecter")
if ord(x)==97 or ord(x)==101 or ord(x)==105 or ord(x)==111 or ord(x)==117 or ord(x)==65 or ord(x)==69 or ord(x)==73 or ord(x)==79 or ord(x)==85:
    print("Given charecter is vowel")
else:
    print("Given charecter is not vowel")
output-
Enter charecterE
Given charecter is vowel
'''
#Q9 input any charecter and check wether it is alfabet,number or special charecter.
'''x=(input("Enter a charecter"))
if 90>=ord(x)>=65 or 97<=ord(x)<=122:
    print(x,"Given charecter is alfabet")
elif 48<=ord(x)<=59:
    print(x,"Given charecter is number....")
else:
    print(x,"Given charecter is special charecter.....")

output-
RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter a charecter5
5 Given charecter is number....

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter a charecter*
* Given charecter is special charecter.....
'''
#10 check whether a charechter is uppercase or lower case alfabet
'''x=input("Enter an alfabet")
if 90>=ord(x)>=65:
    print("Given alfabet is Upper case")
elif 97<=ord(x)<=122:
    print("Given alfabet is lower case")
output-
================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter an alfabets
Given alfabet is lower case

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter an alfabetD
Given alfabet is Upper case
'''
#Q11 input week number and print week day
'''x=int(input("Enter week number"))
if x==1:
    print(x,"=","Sunday")
elif x==2:
    print(x,"=","monday")
elif x==3:
    print(x,"=","tuesday")
elif x==4:
    print(x,"=","wednesday")
elif x==5:
    print(x,"=","thursday")
elif x==6:
    print(x,"=","friday")
elif x==7:
    print(x,"=","saturday")
output-
================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter week number2
2 = monday

================= RESTART: C:/Users/student/Desktop/day 2 task.py ================
Enter week number6
6 = friday
'''
#Q 21 input electricity unit charges and calculate total electricity bill acc0ordingly to the given conditions:
