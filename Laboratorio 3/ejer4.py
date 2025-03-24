import turtle

v = turtle.Screen()
t = turtle.Turtle()

#direccion del cursor 
t.up()
t.goto(-150,-100)
t.down()
#Esto es para el recuadro 
t.fillcolor("yellow")
t.begin_fill()
t.pensize(5)
t.fd(300)
t.left(90)
t.fd(300)
t.left(90)
t.fd(300)
t.left(90)
t.fd(300)
t.left(90)
t.end_fill()

#esto es para las letra N 
t.pensize(15)
t.up()
t.fd(50)
t.left(90)
t.fd(50)
t.down()
t.color("red")
t.fd(200)
t.left(200)
t.fd(210)
t.left(160)
t.fd(200)

#para la letra L
t.left(270)
t.up()
t.fd(50)
t.down()
t.left(270)
t.fd(200)
t.left(90)
t.fd(80)

turtle.done()