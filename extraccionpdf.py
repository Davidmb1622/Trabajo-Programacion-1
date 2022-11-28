from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from PIL import Image
from datetime import datetime


#como tenemso que tener la pagina en A4
w, h = A4
c = canvas.Canvas("extracciones.pdf", pagesize=A4)
print(A4)
#abrir imagen para que la reconozca
Image.open('cabimtex.png')
c.drawImage('cabimtex.png', 130, 600, 315, 170)
#textos
#titulo
c.setFont('Helvetica-Bold', 20)
c.drawString(120, 570, "INFORME DE LAS EXTRACCIONES")

#pie de página
c.setFont('Helvetica', 12)
c.drawString(500, 50,'Page#1')

#texto oculto y extracción
text= c.beginText(65,500)
text.setFont('Helvetica', 12)
text.textLines('-> Extracción del Texto Oculto\n'
              'La pelota es roja.')
text.textLines('-> Extracción del Texto estampado en la imagen\n'
              'Los textos prescriptivos.')
c.drawText(text)

#extracciones de cadena de caracteres
now = datetime.now()
c.setFont('Helvetica', 12)
c.drawString(65, 390, f"Las extracciones se realiaron el {now.date()}")
c.drawString(65, 370, f"Las extracciones se realiaron el {now.date()}")

c.showPage()
c.save()


#extraciones realizadas el

