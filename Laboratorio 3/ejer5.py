import turtle

v = turtle.Screen()
t = turtle.Turtle()

t.speed(10)

#direccion del cursor 
t.up()
t.goto(-300,100)
t.down()

#triangulo
t.fillcolor("skyblue")
t.begin_fill()
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.end_fill()

#salto de linea
t.up()
t.fd(140)
t.down()

#cuadrado
t.fillcolor("red")
t.begin_fill()
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.end_fill()

#salto de linea
t.up()
t.fd(140)
t.down()

#rectangulo
t.fillcolor("yellow")
t.begin_fill()
t.fd(150)
t.left(90)
t.fd(100)
t.left(90)
t.fd(150)
t.left(90)
t.fd(100)
t.left(90)
t.end_fill()

#salto de linea
t.up()
t.fd(240)
t.down()

#circulo
t.fillcolor("green")
t.begin_fill()
t.circle(50)  
t.end_fill()

#direccion del cursor 
t.up()
t.goto(-250,-70)
t.down()

#rombo
t.fillcolor("yellow")
t.begin_fill()
t.left(45)
t.fd(70)
t.left(90)
t.fd(70)
t.left(90)
t.fd(70)
t.left(90)
t.fd(70)
t.end_fill()

#direccion del cursor 
t.up()
t.left(45)
t.goto(-180,-70)
t.down()

#romboide
t.fillcolor("sky blue")
t.begin_fill()
t.fd(90)
t.left(75)
t.fd(90)
t.left(105)
t.fd(90)
t.left(75)
t.fd(90)
t.end_fill()

#direccion del cursor 
t.up()
t.left(105)
t.goto(10,-70)
t.down()

#trapecio
t.fillcolor("green")
t.begin_fill()
t.fd(100)
t.left(65)
t.fd(100)
t.left(115)
t.fd(180)
t.left(112)
t.fd(97)
t.left(70)
t.end_fill()

#salto de linea
t.up()
t.goto(240,-35)
t.down()

#ovalo
t.fillcolor("red")
t.begin_fill()
t.shape("circle")
t.shapesize(4, 7, 1)
t.end_fill()

turtle.done()
