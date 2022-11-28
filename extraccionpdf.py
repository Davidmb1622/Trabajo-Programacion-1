from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

#como tenemso que tener la pagina en A4
w, h = A4
c = canvas.Canvas("extracciones.pdf", pagesize=A4)

#imagen
c.drawImage('cabimtex.png', 50, h - 200, width=50, height=50)
c = canvas.Canvas("cabimtex.png", pagesize=A4)
# Ubicar el logo en el extremo superior izquierdo.
img = ImageReader("cabimtex.png")
# Obtener el ancho y alto de la imagen.
img_w, img_h = img.getSize()
# h - img_h es el alto de la hoja menos el alto
# de la imagen.
c.drawImage(img, 0, h - img_h)
c.save()

#textos
#titulo
c.drawString(50, h - 50, "INFORME DE LAS EXTRACCIONES")
#CUERPO DE TEXTO COMPELTO

text = c.beginText(50, h - 50)
c.setFont("Lora", 20)
text.textLine('')


c.showPage()
c.save()
