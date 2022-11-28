'''
Al entrar en esta opción, la función recibirá como parámetro el fichero de la imagen
modificada, [proyimod1T.png], conteniendo el texto insertado en la opción anterior.
Tal como se describe a continuación, lo primero que hará será mostrar el nombre del mismo.
Seguidamente, el programa dejará constancia del proceso de extracción del texto oculto en la imagen, indicando en
pantalla el contenido del texto extraído. Dicho texto extraído deberá almacenarse en un fichero
denominado extraccion.txt.
Como puede observarse a medida que se ejecutan las operaciones, aparece en la pantalla un
reflejo de cada una de ellas
'''

from PIL import Image
import cv2 as cv2
from stegano import lsb

def menu():
    #mientras sea verdad
    while True:
        #imprimir
        print('\n'
            '1) Insertar mensaje oculto en una imagen\n'
            '2) Extraer mensaje oculto de una imagen\n'
              )
        #Pedimos al usuario que elija una opción
        opcion = int(input('Opción: '))
        #si es uno
        if opcion == 1:
            # Título
            print("\nOPCIÓN: Insertar mensaje oculto en una imagen")
            texto_oculto()
        #si es dos
        elif opcion == 2:
            # Título
            print("\nOPCIÓN:  Extraer mensaje oculto de una imagen")
            extraer_oculto(oculta)
        else:
            print('error')

def texto_oculto():

    original = 'img/proyimag1T.png'
    oculta = 'img/proyimod1T.png'
    img_ori = cv2.imread(original)
    men_secreto = input('\nIntroduzca el mensaje de texto a ocultar: ')
    secret = lsb.hide(original, men_secreto).save(oculta)

    return oculta

#--------------------------
def extraer_oculto(oculta):

    print(f'El fichero de la imagen con texto oculto se llama: {oculta}')
    m_secret = lsb.reveal(oculta)
    print('Exrayendo el texto de la imagen...')
    print(f'El texto oculto es: {m_secret}')

    with open('extraccion.txt', 'w+') as secreto:
        secreto.write(m_secret)


if __name__ == "__main__":
    menu()