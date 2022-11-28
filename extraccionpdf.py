from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

w, h = A4
c = canvas.Canvas("extracciones.pdf", pagesize=A4)
c.drawString(50, h - 50, "¡Hola, mundo!")
c.showPage()
c.save()
https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/