from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import magenta, red
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from PIL import Image
from datetime import datetime



'''''
with open('extraccio.txt', 'w') as secreto:
    secreto.writelines(['-> Extracción del Texto estampado en la imagen\n',
                        'La pelota es roja.\n',
                        '-> Extracción del Texto Oculto\n',
                        'Los textos prescriptivos.\n'])

with open('extraccio.txt') as read:
    extrac1 = read.read()
print(extrac1)

#abrimos el documento donde están las extracciones
with open('extraccion.txt', 'r') as read:
    extrac = read.read()
print(extrac)
#invocamos el ancho y el alto A4
w, h = A4
#creamos la variable con la que invocaremos al pdf
c = canvas.Canvas("extracciones.pdf", pagesize=A4)
print(A4)
#abrir imagen para que la reconozca
Image.open('cabimtex.png')
c.drawImage('cabimtex.png', 130, 600, 315, 170)
#textos
#titulo
c.setFont('Helvetica-Bold', 20)
c.drawString(120, 570, "INFORME DE LAS EXTRACCIONES")

#extracción del documento txt
#creamos una lista vacia para meter el texto oculto y el texto estampado
cadenas= []
y = 500
#y2= 370
for line in extrac.split('\n'):
    c.setFont("Helvetica", 12)
    if not line.startswith('->'):
        line.removesuffix(".")
        cadenas.append(line)
        #c.drawString(65, y2, f"El texto oculto consta de {str(len(line))} caracteres")
        #y2 = y2-20
    c.drawString(65, y, line)
    y = y - 13

#Extracciones de la cuenta de caracteres y palabras de ambos textos
#Ponemos en una variable la fecha del sistema
fecha = datetime.now()
#declaramos el tamaño y la fuente de letra que usaremos
c.setFont('Helvetica', 12)
c.drawString(65, 390, f"Las extracciones se realiaron el {fecha.date()}")
c.drawString(65, 370, f"El texto oculto consta de {len(cadenas[0][:-1])} caracteres.")
c.drawString(65, 350, f"El texto estampado consta de {len(cadenas[1][:-1])} caracteres.")
c.drawString(65,330, f"El texto oculto está compuesto de {len(cadenas[0].split())} palabras.")
c.drawString(65,310, f"El texto estampado está compuesto de {len(cadenas[1].split())} palabras.")

#extracciones de cadena de caracteres
#para poder ver la fecha del sistema

#pie de página
c.setFont('Helvetica', 12)
#Imprimimos el pie de página
c.drawString(500, 50,'Page#1')
#paara poder ver la página
c.showPage()
#Slava la página
c.save()
'''
#https://stackoverflow.com/questions/47001123/generated-pdf-report-in-reportlab-is-not-similar-to-original-text-data
#https://stackoverflow.com/questions/69702682/counting-the-total-number-of-lines-except-the-ones-that-start-with-a-special-cha

#texto oculto y extracción
#text= c.beginText(65,500)
#text.setFont('Helvetica', 12)


print('\n\t\tGenerando un PDF con la información...\n')

# abrimos el documento donde están las extracciones
with open('extraccion.txt', 'r') as read:
    extrac = read.read()
# invocamos el ancho y el alto A4
w, h = A4
# creamos la variable con la que invocaremos al pdf
c = canvas.Canvas("extracciones.pdf", pagesize=A4)
# abrir imagen para que la reconozca
Image.open('cabimtex.png')
c.drawImage('cabimtex.png', 130, 600, 315, 170)
# textos
# titulo
c.setFont('Helvetica-Bold', 20)
c.drawString(120, 570, "INFORME DE LAS EXTRACCIONES")
# extracción del documento txt
# creamos una lista vacia para meter el texto oculto y el texto estampado
cadenas = []
# Creamos una variable que sera donde empieze el texto de extraccion.txt
y = 510
# y2= 370
# recorremos palabra por palabras hasta los saltos creando lineas
for line in extrac.split('\n'):
    # le damos tamaño y fuente a la letra
    c.setFont("Helvetica", 13)
    # dibujamos todas las lineas del documento en el pdf
    c.drawString(65, y, line)
    # con cada vuelta imprime 13 pixeles más abajo
    y = y - 13.5
    # si las lineas empiezan por -> ignorar
    if not line.startswith('->'):
        # añadimos a la lista las dos frases que necesitamos y las separamos en una variable
        cadenas.append(line)
        # c.drawString(65, y2, f"El texto oculto consta de {str(len(line))} caracteres")
        # y2 = y2-20

# Extracciones de la cuenta de caracteres y palabras de ambos textos con la variable en donde se encuentran
# Ponemos en una variable la fecha del sistema
fecha = datetime.now()
# declaramos el tamaño y la fuente de letra que usaremos
c.setFont('Helvetica', 13)
# definimos de donde sale la primera frase
# imprimimos primero la fecha
c.drawString(65, 410, f"Las extracciones se realiaron el {fecha.date()}.")
# imprimimos la cantidad de caracteres del texto oculto
c.drawString(65, 390, f"El texto oculto consta de {len(cadenas[0][:-1])} caracteres.")
# imprimimos la cantidad de caracteres del texto estampado
c.drawString(65, 370, f"El texto estampado consta de {len(cadenas[1][:-1])} caracteres.")
# imprimimos la cantidad de palabras del texto oculto
c.drawString(65, 350, f"El texto oculto está compuesto de {len(cadenas[0].split())} palabras.")
# imprimimos la cantidad de palabras del texto estampado
c.drawString(65, 330, f"El texto estampado está compuesto de {len(cadenas[1].split())} palabras.")
# pie de página
c.setFont('Helvetica', 12)
# Imprimimos el pie de página
c.drawString(500, 50, 'Page#1')
# paara poder ver la página
c.showPage()
# Salva la página
c.save()