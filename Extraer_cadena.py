from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from pytesseract import pytesseract


'''
tex_draw = ImageDraw.Draw(img_abierta)
fuente = ImageFont.truetype('fuentes/lato/Lato-Regular.ttf', 65)
tex_draw.text((100,50), "Probando esto", font=fuente,  fill=(0,0,0))
img_abierta.show()
img_texto =img_abierta.save('imagtext1T2.png')
img_texto.show()
with open('extraccion.txt', 'a+') as extraido:
    extraido.write(text[:-1])
'''
imagen = 'imagtext1T.png'
img_abierta = Image.open(imagen)

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img_abierta)

print(type(text[:-1]))
print(text[:-5])#Tiene unos espacios feos que hay que quitar
print(type(text))
print(text)

