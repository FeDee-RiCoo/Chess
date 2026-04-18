# Dizionario pezzi
pezzi = {
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

def DrawPieces(size, t, griglia):
    for riga in range(8):
        for colonna in range(8):
            pezzo = griglia[riga][colonna]
            if pezzo != None:
                x = (colonna - 4) * size + size/2
                y = (3 - riga) * size
                t.penup()
                t.goto(x, y)
                if "bianc" in pezzo:
                    t.color("pink")
                else:
                    t.color("green")
                t.write(pezzi[pezzo], align="center", font=("Comfortaa", 36, "normal"))



