import math 
import turtle
a,b = map(float,input () .split())
c = float(input())

area = round(math.pi*(c*2),2)

v=turtle.Screen()
t= turtle.Turtle()

t.shape("classic")
t.up()
t.goto(a,b)
t.down()
t.color("red")
t.write(str(area))
t.up()
t.goto(a,b-c)
t.down()
t.circle(c)
v.exitonclick()

turtle.done()
