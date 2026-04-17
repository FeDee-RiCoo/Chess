import turtle

def DrawSquare(size,t):
    for i in range (4):
        t.forward(size)
        t.left(90)

def WriteLetters(size,t):
    t.penup()
    # Variabile counter per il codice ASCII
    ascii = 0
    for i in range(-4,4):
        # Partiamo a scrivere la prima lettera dalla meta delle x e meta y
        t.goto((i*size + size/2), (-4*size - size/2))
        t.color("white")
        t.write(chr(65+ascii), font=("Comfortaa", 8, "bold"))
        ascii +=1

def WriteNumbers(size,t):
    t.penup()
    n = 1
    for i in range(-4,4):
        # Partiamo a scrivere la prima lettera dalla meta delle y e meta x
        t.goto((-4*size - size/2), (i*size + size/2))
        t.color("white")
        t.write(n, font=("Comfortaa", 8, "bold"))
        n +=1

def DrawBoard(size,t):
    t.penup()
    # Ciclo che va in ogni punto x della cella
    for i in range (-4,4):
        # Ciclo che va in ogni punto y della cella
        for j in range(-4,4):
            # Posizione di partenza in basso a sinistra
            t.goto(j*size, i*size)
            t.pendown()
            # Se le x sono pari
            if(i % 2 == 0):
                # Se anche le y sono pari procedo a riempire il quadrato
                if(j % 2 == 0):
                    t.fillcolor("black")
                    t.begin_fill()
                    DrawSquare(size,t)
                    t.end_fill()
                    t.penup()
                else:
                    # Se le y sono dispari procedo a riempire il quadrato di bianco
                    t.fillcolor("white")
                    t.begin_fill()
                    DrawSquare(size,t)
                    t.end_fill()
                    t.penup()
            # Se le x sono dispari
            else:
                # Se anche le y sono dipari procedo a riempire il quadrato di nero
                if(j % 2 != 0):
                    t.fillcolor("black")
                    t.begin_fill()
                    DrawSquare(size,t)
                    t.end_fill()
                    t.penup()
                else:
                    # Se le y sono spari procedo a riempire il quadrato di bianco
                    t.fillcolor("white")
                    t.begin_fill()
                    DrawSquare(size,t)
                    t.end_fill()
                    t.penup()



