#importamos las blibiotecas
#Pil para imagenes nos ayudará a comparar las imagenes en el ejercicio 1
from PIL import Image
#cv2 nos ayudara a mostrar las imagenes en una ventana emergente y controlar los tamaños y el color de las imágenes
import cv2 as cv2
#stegano nos permite introducir secretos y descifrarlos
from stegano import lsb



#Definimos el menu de nuestro proyecto
def menu():
    #mientras sea verdad
    while True:
        #imprimir
        print('\n'
            '1) Insertar mensaje oculto en una imagen\n'
            '2) Extraer mensaje oculto de una imagen\n'
            '3) Convertir la imagen a escala de grises\n'
            '4) Extraer cadena visible en una imagen\n'
            '5) Informe de las extracciones (PDF)\n'
            '6) Salir'
        )
        #Pedimos al usuario que elija una opción
        opcion = input('Opción: ')
        #si es uno
        if opcion == '1':
            # Título
            print("\nOPCIÓN: Insertar mensaje oculto en una imagen")
            oculta=texto_oculto()
        #si es dos
        elif opcion == '2':
            # Título
            print("\nOPCIÓN:  Extraer mensaje oculto de una imagen")
            extraer_oculto(oculta)
        #si es tres
        elif opcion == '3':
            # Título
            print("\nOPCIÓN:  Convertir la imagen a escala de grises")
        elif opcion == '4':
            # Título
            print("\nOPCIÓN:  Extraer cadena visible en una imagen")
        elif opcion == '5':
            # Título
            print("\nOPCIÓN:Informe de las extracciones (PDF)")
        elif opcion == '6':
            break
        else:
            print('\nSólo se aceptan número incluidos dentro del menú\n')





#debemos ocultar un mensaje en una imagen
def texto_oculto():

    #Declaramos primero las imágenes que usaremos
    original = 'proyimag1T.png'
    oculta = 'proyimod1T.png'
    #Con ayuda del cv2 haemos que nos lea la imagen
    img_ori = cv2.imread(original)
    #Aquí le decimos que lea el alto y el ancho
    wid = img_ori.shape[1]
    hgt = img_ori.shape[0]
    #Y aquí que imprima esos datos
    print(f'\n{original} tiene {str(wid)} de ancho y de {str(hgt)} alto')
    #Mostramos la imágen en una ventana emergente
    cv2.imshow('Imagen original', img_ori)
    #El waitKey nos permite mantener la imagen hasta que cerremos la ventana
    cv2.waitKey(0)
    #Pedimos al usuario que ponga el mensaje secreto que desee ocultar en la imagen
    men_secreto = input('\nIntroduzca el mensaje de texto a ocultar: ')
    #guardamos el mensaje secreto
    secret = lsb.hide(original, men_secreto).save(oculta)
    #e indicamos que estamos insertandolo
    print('\nInsertando texto en la imagen...')
    #Para poder comparar los bytes de la imagenes usamos el método open importado de la libreria Image de PIL
    # lo hacemos con la imagen original y con la imagen que tiene el mensaje oculto
    ori_img = Image.open(original)
    ocul_img = Image.open(oculta)
    #Si la original es distinta a la de la imagen oculta entonces
    if ori_img != ocul_img:
        #Leemos la imagen que oculta el texto con cv2 e indicamos que el fichero es distinto
        img_oculta = cv2.imread(oculta)
        print(f'\nEl fichero {original} es diferente a {oculta}')
        #Para poder mostrarla por la ventana emergente
        cv2.imshow('Con texto oculto', img_oculta)
        #Le pedimos que espere hasta que nosotros la cerremos
        cv2.waitKey(0)

    return oculta


def extraer_oculto(oculta):
    print('')
    #la imagen con el texto oculto anterior lo traemos
    print(f'El fichero de la imagen con texto oculto se llama: {oculta}')
    #revelamos su secreto y lo imprimimos
    m_secret = lsb.reveal(oculta)
    print('Exrayendo el texto de la imagen...')
    print(f'El texto oculto es: {m_secret}')
    #por último guardamos el secreto en un fihero llamado extracción.txt
    with open('extraccion.txt', 'w+') as secreto:
        secreto.write(m_secret)





if __name__ == "__main__":
    menu()