import turtle
from board import DrawBoard, WriteLetters, WriteNumbers
from pieces import DrawPieces

CELL_SIZE = 60

griglia = [
    ["torre_nera", "cavallo_nero", "alfiere_nero", "regina_nera", "re_nero", "alfiere_nero", "cavallo_nero","torre_nera"],
    ["pedone_nero", "pedone_nero", "pedone_nero", "pedone_nero", "pedone_nero", "pedone_nero", "pedone_nero", "pedone_nero", ],
    [None, None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, None, ],
    [None, None, None, None, None, None, None, None, ],
    ["pedone_bianco", "pedone_bianco", "pedone_bianco", "pedone_bianco", "pedone_bianco", "pedone_bianco", "pedone_bianco", "pedone_bianco", ],
    ["torre_bianca", "cavallo_bianco", "alfiere_bianco", "regina_bianca", "re_bianco", "alfiere_bianco", "cavallo_bianco","torre_bianca"]
]
pezzo_selezionato = None
cella_selezionata = None
def OnClick(x, y, t):
    print(f"Click su x:{x} y:{y}")
    global pezzo_selezionato, cella_selezionata, griglia
    # Conversione da pixel a riga e colonna
    riga = int(((-y) + 4*CELL_SIZE) / CELL_SIZE)
    colonna = int((x + 4*CELL_SIZE) / CELL_SIZE)
    print(f"Riga:{riga} Colonna:{colonna}")
    print(f"Cella: {griglia[riga][colonna]}")
    # Se il pezzo selezionato è None si è al Primo Click
    if pezzo_selezionato == None:
        # Se c'è effettivamente un pezzo nella cella cliccata
        if griglia[riga][colonna] != None:
            pezzo_selezionato = griglia[riga][colonna]
            cella_selezionata = (riga,colonna)
    # Il pezzo è gia stato selezionato e ci si trova al secondo Click        
    else:
        # Impostare nuova posizione per il pezzo
        print("SECONDO CLICK - sposto il pezzo")
        griglia[riga][colonna] = pezzo_selezionato
        # Reset della cella selezionata
        griglia[cella_selezionata[0]][cella_selezionata[1]] = None
        pezzo_selezionato = None
        cella_selezionata = None
        t.clear()
        t.penup()
        turtle.bgcolor("#262522")
        turtle.tracer(0)
        DrawBoard(CELL_SIZE, t)
        WriteLetters(CELL_SIZE, t)
        WriteNumbers(CELL_SIZE, t)
        DrawPieces(CELL_SIZE, t, griglia)
        turtle.update()


        


        