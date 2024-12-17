import turtle

turtle.up()
turtle.speed(0)

i = 0
while i < 6:
    turtle.goto(-500, i * 100)
    turtle.down()
    turtle.goto(500, i * 100)
    turtle.up()
    i += 1

i = 0
while i < 6:
    turtle.goto(i * 200 - 500, 0)
    turtle.down()
    turtle.goto(i * 200 - 500, 500)
    turtle.up()
    i += 1


turtle.teleport(-400, 250)
turtle.write("Jaskinia", align="center")

turtle.teleport(0, 450)
turtle.write("Zamek", align="center")

turtle.color("green")
turtle.teleport(400, 150)
turtle.write("Las", align="center")

turtle.color("red")
turtle.teleport(200, 250)
turtle.write("Miasto", align="center")

turtle.color("black")
turtle.teleport(0, 50)
turtle.seth(90)
turtle.done()
