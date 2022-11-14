from numpy import random
import pandas as pd
from numpy.ma import count


#1. Crea una archivo python que muestre 10 números aleatorios entre 1 y 100 y los muestre ordenados
def aleatorios():
    for i in range(10):
        print(random.randint(1,100))
#aleatorios()
#2. Crea otro archivo python que pida una frase y responda cuántas veces está la letra que hayas elegido
def contar():
    cuentame=input('dime una frase : ')
    letra=input('dime la letra que quieres contar: ')
    print(f'la frase tiene {cuentame.count(letra)} ')
#contar()
#3. Busca un archivo csv en internet y muestra un gráfico circular que muestre los datos
def grafico():
    datos = pd.read_csv('D:\\adrian\\programacion\\deberes\\actividad15\\local-comercial-farmacias.csv')
    df = datos[["codigoCNAE","streetAddress","postalCode"]]


grafico()
#4. Este proyecto, sus archivos, lo subes a un repositorio Github.
