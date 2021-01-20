import string
import numpy as np
import matplotlib.pyplot as plt
import guizero as gui

def grafico():
    f = open(nome_file.value, 'r')

    coordX = []
    coordY = []
    
    for riga in f:
        valori = str(riga)  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y

    f.close()  # chiudiamo il file

    # ordiniamo le liste
    coordX.sort()
    coordY.sort()

    # ora sono pronte per essere usate anche nei grafici

    plt.scatter(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()
    
root = gui.App(title="Grafico", height=62, width=300)

nome_file = gui.TextBox(root, text="Inserisci nome file", width='fill')

bottone = gui.PushButton(root,command =grafico,  text="Genera il grafico",width='fill')

root.display()
