from turtle import *
from random import randrange, choice
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colores = ["purple","red", "blue", "yellow"]
serpiente = choice(colores)
comida = choice(colores)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    #if abs(head-food) < 10:
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        global serpiente
        global comida
        serpiente = choice(colores)
        comida = choice(colores)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, serpiente)

    square(food.x, food.y, 9, comida)
    update()
    ontimer(move, 100)

def moveFood():
    food.x+=randrange(-10,11,10)
    food.y+=randrange(-10,11,10)
    ontimer(moveFood,1000)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
moveFood()
done()
