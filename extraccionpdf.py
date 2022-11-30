from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.colors import magenta, red
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from PIL import Image
from datetime import datetime

with open('extraccio.txt', 'w') as secreto:
    secreto.write('-> Extracción del Texto stampado en la imagen')
    secreto.write('La pelota es roja.')
    secreto.write('-> Extracción del Texto Oculto')
    secreto.write('Los textos prescriptivos.')
with open('extraccion.txt') as read:
    extrac1=read.read()


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

y = 500
y2= 370
for line in extrac.split('\n'):
    c.setFont("Helvetica", 12)
    if not line.startswith('->'):
        lineas = line
        c.drawString(65, y2, f"El texto oculto consta de {str(len(line))} caracteres")
        y2 = y2-20
    c.drawString(65, y, line)
    y = y - 13

for lines in extrac1:
    c.setFont("Helvetica", 12)
    c.drawString(65, 200, lines)


#for count in extrac.split('\n'):


#extracciones de cadena de caracteres
#para poder ver la fecha del sistema
fecha = datetime.now()
c.setFont('Helvetica', 12)
c.drawString(65, 390, f"Las extracciones se realiaron el {fecha.date()}")


#pie de página
c.setFont('Helvetica', 12)
#Imprimimos el pie de página
c.drawString(500, 50,'Page#1')
#paara poder ver la página
c.showPage()
#Slava la página
c.save()


#https://stackoverflow.com/questions/47001123/generated-pdf-report-in-reportlab-is-not-similar-to-original-text-data
#https://stackoverflow.com/questions/69702682/counting-the-total-number-of-lines-except-the-ones-that-start-with-a-special-cha

#texto oculto y extracción
#text= c.beginText(65,500)
#text.setFont('Helvetica', 12)