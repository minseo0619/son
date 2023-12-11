# import streamlit as st
import streamlit as st
# import random 
import matplotlib.pyplot as plt
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:
    c1 = st.radio('선의 색을 선택하시오', ['red', 'green', 'blue', 'orange'])
with col2:
    s1 = st.radio('선의 색을 선택하시오', ['--', '-.'])
with col3:
    m1 = st.radio('마커의 형태를 선택하시오', ['o', '^', 's', 'p'])

fig, ax = plt.subplots()

x = []
y = []
for i in range(-20,21, 2):
    x.append(i)
    y.append(-2*i*i + 3*i +5)

# plt.plot(x,y'r:h')
plt.plot(x, y, color=c1, linestyle=s1, marker=m1)

st.pyplot(fig)


import sys
sys.exit()


x = []
y = []
ysin = []
for i  in range(-20, 21, 1):
    x.append(i)
    y.append(3*i*i - 5*i +2)
    ysin.append(1200*np.sin(i))
# x    

plt.plot(x, y, '--rs', label = '2nd Equation')
plt.plot(x, ysin, '--go', label = 'sin Function')
plt.legend()
plt.xlabel('x.axis')
plt.ylabel('y.axis')
plt.xlim([-15, 15])
plt.ylim([-2000, 2000])

st.pyplot(fig)

import sys
sys.exit()


# import time
# import random as r

# import turtle
# t = turtle.Turtle()
# t.shape('turtle')

# def tree(length):
#     if length > 5:
#         t.forward(length)
#         t.right(20)
#         tree(length-15)
#         t.left(40)
#         tree(length-15)
#         t.right(20)
#         t.backward(length)

# t = turtle.Turtle()
# t.left(90)

# t.color('green')
# t.speed(0)
# tree(90)

# import random
# t = turtle.Turtle()
# t.shape('turtle')
# # t.color((77/255, 239/255, 93/255))
# # t.forward(100)


# t.speed(0)
# t.pensize(5)
# t.goto(0,0)
# while True:
#     for i in range(30):
#         # t.circle(1+5*i)
#         t.forward(1 + 5*i)
#         t.left(90)
#         t.forward(1 + 5*i)
#         t.left(90) 
#         t.forward(1 + 5*i)
#         t.left(90)
#         t.forward(1 + 5*i)
#         t.left(90)
#         t.color((r.random(),r.random(),r.random()))
#         t.goto(i*20, 0)
#     t.clear()

# turtle.done()


# screen = turtle.Screen()
# im1 = 'rabbit.jpg'

# t1 = turtle.Turtle()
# t2 = turtle.Turtle()
# t3 = turtle.Turtle()

# # screen.addshape(im1)
# t1.shape('turtle')
# t2.shape('turtle')
# t3.shape('turtle')


# t1.penup()
# t1.shapesize(3)
# t1.pensize(5)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.pensize(5)
# t2.goto(-300,-100)

# t3.penup()
# t3.shapesize(3)
# t3.pensize(5)
# t3.goto(-300,-300)

# t1.pendown()
# t2.pendown()
# t3.pendown()
# t1.speed(1)
# t2.speed(1)
# t3.speed(1)


# for i in range(50):
#     d1 = r.randint(1, 30)
#     t1.forward(d1)
#     d2 = r.randint(1, 30)
#     t2.forward(d2)
#     d3 = r.randint(1, 30)
#     t3.forward(d3)


# ai = random.randidnt(1, 45)
# ai



# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed()

# def rec(x,y, lx, ly):
#     t.up()
#     t.goto(x,y)
#     t.down()
#     for i in range (2):
#         t.forward(lx)
#         t.left(90)
#         t.forward(ly)
#         t.left(90)



# rec(-200, 0, 100, 50)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 100)



# turtle.done()




# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# t= turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.width(3)
# length = 10
# while length < 500:
#     t.forward(length)
#     t.pencolor(colors[length%6])
#     t.right (89)
#     length +=5


# turtle.done()

# def user_sum(n):
#     s = 0
#     for i in range(1, n+1):
#         s = s+i
#     s

# user_sum(100)
# user_sum(200)


# 'apple'+'grape'

# age=20
# if age < 20:
#     print('aa')
# else:
#     print('bb')




# for i in range(100):
#     t.forward(length)
#     t.left(90)
#     t.width(3)
#     t,pencolor('blue')

#     length += 5

# n= 20
# ang= 360/n
# for i in range(n):
#     t.circle(80) # :픽셀(반지름)
#     t.left(ang)   # : 각도


# turtle.done()



# for i in range(1, 10):
#     if i %3 ==1:
#         i





# s=0 #초기값
# for i in range (1, 100, 2):
#     's=', s, 'i=', 1
#     s=s+i
#     x=100
#     x+=5
#     x-=10 
#     s +=i
#     's+i=', s    







# '7과 4의 산술 연산'
# '덧셈', 7+4
# '뺄셈', 7-4
# '곱셈', 7*4
# '나눗셈', 7/4
# '몫', 7//4
# '나머지', 7%4
# '거듭제곱', 2**4




# import turtle
# t= turtle.Turtle()
# t.shape('turtle')

# turtle.done()







# st.write('스트림릿.....')

# st.image('streamlit image')
# st.image('im.jpg')
#a=3.141592*10*10.0
#b=(1/100)*1234

# print('Hello')
# st.write('Helddfsdflo')
# st.write('Helddfsdflo')
# st.write('강아지'+'고양이')
# st.write('1+1')
# st.write(1+1)

#print (a, b)
#a, b
import streamlit as st
# import random 
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = []
y = []
for i  in range(-20, 21, 5):
    x.append(i)
    y.append(3*i*i - 5*i +2)
# x    

plt.plot(x, y, '-yo')
st.pyplot(fig)



# numbers = []
# for i  in range(10):
#     numbers.append('random.randint(1,10)')

# numbers
# plt.plot(numbers)
# plt.ylabel('som random numbers')
# x = []
# for i in range(-100, 100):
#     x.append(i/10.0)

# col = st.columns(3)
# with col(0):
#     a = st.number_input('insert a' step = 1)

# with col(1):
#     b = st.number_input('insert b' step = 1)
# with col(2):
#     c = st.number_input('insert c' step = 1)
# y = []
# for i in x:
#     y.append(a*i**2+b*i+c)
# plt.plot(x, y)

# st.pyplot(fig)