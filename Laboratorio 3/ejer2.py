import turtle

v = turtle.Screen()
t = turtle.Turtle()

t.shape("arrow")
t.color("red")
t.pensize(12)
t.fd(50)
t.stamp()
t.up()
t.fd(40)
t.left(90)
t.fd(40)
t.down()

t.shape("arrow")
t.color("yellow")
t.fd(50)
t.stamp()
t.up()
t.fd(40)
t.left(90)
t.fd(40)
t.down()

t.shape("arrow")
t.color("green")
t.fd(50)
t.stamp()
t.up()
t.fd(40)
t.left(90)
t.fd(40)
t.down()

t.shape("arrow")
t.color("blue")
t.fd(40)
t.stamp()


turtle.done()

