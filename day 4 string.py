s_1='nuts and bolts in python program'
s_2='now python is easy'
#Q1)addition
#i)add S_1+S_2
'''print(s_1+s_2)
output-
nuts and bolds in python programnow python is easy'''
#ii)find s_1+'$%$%'+s_2
'''print(s_1+'$%$%'+s_2)
output-
nuts and bolds in python program$%$%now python is easy
'''
#Q2)repetition
#find= s_2*2,s_2*-2,s_2*0,s_2*1.2
'''print(s_2*2)
output-
now python is easynow python is easy
'''
'''print(s_2*-2)
output-
'''
'''print(s_2*0)
output-
'''
'''print(s_2*1.2)
output-
Traceback (most recent call last):
  File "C:/Users/student/Desktop/day 4 string.py", line 25, in <module>
    print(s_2*1.2)
TypeError: can't multiply sequence by non-int of type 'float'
'''
#Q3 find len(s_1),len(s_2)
'''print(len(s_1))
output-
32
'''
'''print(len(s_2))
output-
18
'''
#Q4 find s_1[2:4],s_2[-1:]s_1[0:-1],s_1[-5],s_2[1:4]
'''print(s_1[2:4])
output-
ts
'''
'''print(s_2[-1:])
output-
y
'''
'''print(s_1[0:-1])
output-
nuts and bolts in python progra
'''
'''print(s_1[-5])
output-
o
'''
'''print(s_2[1:4])
output-
ow
'''
#Q5) using for loop display each char in new line
'''
for x in s_1:
    print(x)
output-
n
u
t
s
 
a
n
d
 
b
o
l
t
s
 
i
n
 
p
y
t
h
o
n
 
p
r
o
g
r
a
m
'''
#Q6) using while loop display each char in new line.
n=0
