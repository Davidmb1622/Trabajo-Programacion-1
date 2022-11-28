'''Al entrar en esta opción, la función recibirá como parámetro el fichero de la imagen
denominada [proyimag1T.png]. Con ese dato deberá mostrar los píxeles de ancho y alto que tiene
dicho fichero

Seguidamente, el propio programa deberá mostrar por pantalla, en una ventana que
llevará el letrero de “Imagen original” (aunque al desplegarse en la ventana se vea Ima...). A partir de ahí,
solicitará por teclado el texto que se pretende ocultar en el fichero. Al iniciar el proceso de inserción
del texto en la imagen, se deberá indicar en pantalla que éste se está realizando.☼☻☼
'''
from PIL import Image
import cv2 as cv2
from stegano import lsb

# Declaramos primero las imágenes que usaremos
original = 'img\proyimag1T.png'
oculta = 'img\proyimod1T.png'
# Con ayuda del cv2 haemos que nos lea la imagen
img_ori = cv2.imread(original)
# Aquí le decimos que lea el alto y el ancho
wid = img_ori.shape[1]
hgt = img_ori.shape[0]
# Y aquí que imprima esos datos
print(f'\nproyimag1T tiene {str(wid)} de ancho y de {str(hgt)} alto')
# Mostramos la imágen en una ventana emergente
cv2.imshow('Imagen original', img_ori)
# El waitKey nos permite mantener la imagen hasta que cerremos la ventana
cv2.waitKey(0)
# Pedimos al usuario que ponga el mensaje secreto que desee ocultar en la imagen
men_secreto = input('\nIntroduzca el mesanje de texto a ocultar: ')
# guardamos el mensaje secreto
secret = lsb.hide(original, men_secreto).save(oculta)
# e indicamos que estamos insertandolo
print('\nInsertando texto en la imagen...')
# Para poder comparar los bytes de la imagenes usamos el método open importado de la libreria Image de PIL
ori_img = Image.open(original)
# lo hacemos con la imagen original y con la imagen que tiene el mensaje oculto
ocul_img = Image.open(oculta)
# Si la original es distinta a la de la imagen oculta entonces
if ori_img != ocul_img:
    # Leemos la imagen que oculta el texto con cv2
    img_oculta = cv2.imread(oculta)
    # Para poder mostrarla por la ventana emergente
    cv2.imshow('Con texto oculto', img_oculta)
    # Le pedimos que espere hasta que nosotros la cerremos
    cv2.waitKey(0)
    # el fichero es distinto
    print('\nEl fichero proyimag1T.png es diferente a proyimod1T.png')
