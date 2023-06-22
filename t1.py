from turtle import *
speed('fastest')
angle = 360/6
distance = 100
sides = 6
for i in range(sides):
    pencolor('red') # to change the color of pen
    fd(distance)
    rt(360/sides)
    circle(distance/2)
    for i in range(sides):
        fd(distance/2)
        rt(360/sides)
        dot(10)
        write(i)
        for i in range(sides):
            pencolor('blue')
            fd(distance/4)
            rt(360/sides)
hideturtle()#360/6 to get the angle
mainloop() # to keep the window open