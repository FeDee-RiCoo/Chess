import turtle

def DrawSquare(size):
    for i in range (4):
        t.forward(CELL_SIZE)
        t.left(90)

# def FillSquare(size):
    
#     for i in range (4):
#         t.forward(CELL_SIZE)
#         t.left(90)

# Creazione turtle
t = turtle.Turtle()
# Velocità tartaruga
t.speed(10)
# Comando per non aggiornare lo schermo mentre la tartaruga disegna
turtle.tracer(0)
# Nascondimento tartaruga
t.hideturtle()


# Variabile grandezza di ogni cella
CELL_SIZE = 60

t.penup()
# Ciclo che va in ogni punto x della cella
for i in range (-4,4):
    # Ciclo che va in ogni punto y della cella
    for j in range(-4,4):
        # Posizione di partenza in basso a sinistra
        t.goto(j*CELL_SIZE, i*CELL_SIZE)
        t.pendown()
        # Se le x sono pari
        if(i % 2 == 0):
            # Se anche le y sono pari procedo a riempire il quadrato
            if(j % 2 == 0):
                t.fillcolor("black")
                t.begin_fill()
                DrawSquare(CELL_SIZE)
                t.end_fill()
                t.penup()
            else:
                # Se le y sono dispari procedo soltanto a disegnare il quadrato
                DrawSquare(CELL_SIZE)
                t.penup()
        # Se le x sono dispari
        else:
            # Se anche le y sono dipari procedo a riempire il quadrato
            if(j % 2 != 0):
                t.fillcolor("black")
                t.begin_fill()
                DrawSquare(CELL_SIZE)
                t.end_fill()
                t.penup()
            else:
                # Se le y sono spari procedo soltanto a disegnare il quadrato
                DrawSquare(CELL_SIZE)
                t.penup()

# Comando per fare l update dello schermo a disegno finito
turtle.update()

turtle.done() 


