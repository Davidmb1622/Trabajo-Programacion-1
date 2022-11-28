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

#tenemos nuestra imagen
imagen = 'imagtext1T.png'
print(f'El fichero de la imagen se llama: {imagen}')
#la abrimos
img_abierta = Image.open(imagen)
print('Extrayendo el texto de la imagen...')
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

text = pytesseract.image_to_string(img_abierta)[:-5]
print(f'El texto recuperado es: {text}.')
with open('extraccion.txt', 'a+') as secreto:
    secreto.writelines(f'-> Extracción del Texto stampado en la imagen'
                       f'\n{text}.')

