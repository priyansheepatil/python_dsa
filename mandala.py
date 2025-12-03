import turtle

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

t.pencolor("red")

for i in range(60):
    t.circle(80)   # draw a circle
    t.right(6)     # rotate a little

turtle.done()


