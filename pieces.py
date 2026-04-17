# Dizionario pezzi
pieces = {
    "re_bianco": "♚",
    "regina_bianca": "♛",
    "torre_bianca" : "♜",
    "alfiere_bianco" : "♝",
    "cavallo_bianco" : "♞",
    "pedone_bianco" : "♟",
    "re_nero": "♚",
    "regina_nera": "♛",
    "torre_nera" : "♜",
    "alfiere_nero" : "♝",
    "cavallo_nero" : "♞",
    "pedone_nero" : "♟",

}

def DrawPieces(size, t):
    # Pedoni bianchi
    t.penup()
    for i in range(-4,4):
        t.goto((i*size)+(size/2),(-3*size))
        t.color("pink")
        t.write(pieces["pedone_bianco"],align="center", font=("Comfortaa", 36, "normal")) 
    
    # Torri bianche
    t.penup()
    t.goto((-4*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["torre_bianca"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((3*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["torre_bianca"],align="center", font=("Comfortaa", 36, "normal")) 

    # Cavalli bianchi
    t.penup()
    t.goto((-3*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["cavallo_bianco"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((2*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["cavallo_bianco"],align="center", font=("Comfortaa", 36, "normal")) 

    # Alfieri bianchi
    t.penup()
    t.goto((-2*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["alfiere_bianco"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((1*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["alfiere_bianco"],align="center", font=("Comfortaa", 36, "normal")) 

    # Regina bianca
    t.penup()
    t.goto((-1*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["regina_bianca"],align="center", font=("Comfortaa", 36, "normal"))
    
    # Re bianco
    t.penup()
    t.goto((0*size)+(size/2),(-4*size))
    t.color("pink")
    t.write(pieces["re_bianco"],align="center", font=("Comfortaa", 36, "normal"))   
    
    # Pedoni neri
    t.penup()
    for i in range(-4,4):
        t.goto((i*size)+(size/2),(2*size))
        t.color("green")
        t.write(pieces["pedone_nero"],align="center", font=("Comfortaa", 36, "normal"))

    # Torri nere
    t.penup()
    t.goto((-4*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["torre_nera"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((3*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["torre_nera"],align="center", font=("Comfortaa", 36, "normal")) 

    # Cavalli neri
    t.penup()
    t.goto((-3*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["cavallo_nero"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((2*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["cavallo_nero"],align="center", font=("Comfortaa", 36, "normal"))

    # Alfieri neri
    t.penup()
    t.goto((-2*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["alfiere_nero"],align="center", font=("Comfortaa", 36, "normal")) 
    t.goto((1*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["alfiere_nero"],align="center", font=("Comfortaa", 36, "normal"))

    # Regina nera
    t.penup()
    t.goto((-1*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["regina_nera"],align="center", font=("Comfortaa", 36, "normal")) 

    # Re nero
    t.penup()
    t.goto((0*size)+(size/2),(3*size))
    t.color("green")
    t.write(pieces["re_nero"],align="center", font=("Comfortaa", 36, "normal")) 



