import turtle
import game

from board import DrawBoard, WriteLetters, WriteNumbers
from pieces import DrawPieces
from game import OnClick, griglia

# Creazione turtle
t = turtle.Turtle()
# Velocità tartaruga
t.speed(10)
# Comando per non aggiornare lo schermo mentre la tartaruga disegna
turtle.tracer(0)
# Nascondimento tartaruga
t.hideturtle()
# Backgruond grigio
turtle.bgcolor("#262522")


# Variabile grandezza di ogni cella
CELL_SIZE = 60


DrawBoard(CELL_SIZE,t)
WriteLetters(CELL_SIZE,t)
WriteNumbers(CELL_SIZE,t)
DrawPieces(CELL_SIZE, t, game.griglia)

turtle.update()
turtle.onscreenclick(lambda x, y: OnClick(x, y, t))
turtle.done()

