import turtle 
import random

v = turtle.Screen()
t = turtle.Turtle()

t.speed(10)
t.screen.bgcolor("lightblue")

#direccion del cursor 
t.up()
t.goto(-400,-70)
t.down()

#arena
t.fillcolor("orange")
t.begin_fill()
t.fd(800)
t.right(90) 
t.fd(250)
t.right(90)
t.fd(800)
t.right(90)
t.fd(250)
t.right(90)
t.end_fill()

#direccion del cursor 
t.up()
t.goto(-370,250)
t.down()

#el sol
#circulo
t.fillcolor("yellow")
t.begin_fill()
t.circle(70)  
t.end_fill()

#direccion del cursor 
t.up()
t.goto(-300,-140)
t.down()

#arbol1rama
t.fillcolor("brown")
t.begin_fill()
t.fd(40)
t.left(90)
t.fd(100)
t.left(90)
t.fd(40)
t.left(90)
t.fd(100)
t.left(90)
t.end_fill()

#direccion del cursor 
t.up()
t.goto(-275,-50)
t.down()

#arbol1hojas
t.fillcolor("green")
t.begin_fill()
t.circle(70)  
t.end_fill()

#direccion del cursor 
t.up()
t.goto(150,-140)
t.down()

#arbol2rama
t.fillcolor("brown")
t.begin_fill()
t.fd(40)
t.left(90)
t.fd(100)
t.left(90)
t.fd(40)
t.left(90)
t.fd(100)
t.left(90)
t.end_fill()

#direccion del cursor 
t.up()
t.goto(170,-50)
t.down()

#arbol2hojas
t.fillcolor("green")
t.begin_fill()
t.circle(70)  
t.end_fill()

#nubes
def dibujar_circulo(x, y, radio, color):
    turtle.penup()
    turtle.goto(x, y - radio)  
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radio)
    turtle.end_fill()

def dibujar_nube(x, y, tamaño=20):
    for _ in range(5):  
        offset_x = random.randint(-tamaño, tamaño)
        offset_y = random.randint(-tamaño//2, tamaño//2)
        dibujar_circulo(x + offset_x, y + offset_y, tamaño, "white")
turtle.speed(0)

dibujar_nube(200, 200, 30)
dibujar_nube(40, 150, 25)
dibujar_nube(-180, 250, 35)



turtle.done()