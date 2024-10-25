Лекция 11. Модуль Turtle, работа с условными операторами. Черчение жоских рисунков.
python 

# from turtle import *

# def speed_ok():
#     begin_fill()
#     circle(50)
#     end_fill()

# def speed_over():
#     color('yellow')
#     penup()
#     goto(0, -70)
#     goto(-10, -10)
#     pendown()
#     begin_fill()
#     circle(18)
#     end_fill()
#     penup()

# speed = int(input("Скорость транспорта: "))
# if speed <= 60:
#     speed_ok()
# if speed > 60:
#     speed_over()
# hideturtle()
# exitonclick()

from turtle import *

def day():
    color("yellow")
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()

def night():
    color("bisque")
    begin_fill()
    circle(50)
    end_fill()

speed(0)
answer = input("Слышь, чушпан, какое ща время? (утра/вечерочек)? ")
if answer == 'день':
    day()
if answer == 'ночь':
    night()
hideturtle()
exitonclick()
