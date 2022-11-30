#importamos las blibiotecas
#Pil para imagenes nos ayudará a comparar las imagenes en el ejercicio 1
from PIL import Image
#cv2 nos ayudara a mostrar las imagenes en una ventana emergente y controlar los tamaños y el color de las imágenes
import cv2 as cv2
#stegano nos permite introducir secretos y descifrarlos
from stegano import lsb
#permite la extracción de cadenas de caracteres de una imagen
from pytesseract import pytesseract
#importamos esta biblioteca para crear el pdf en una hoja A4
from reportlab.lib.pagesizes import A4
#esta importación sirve para poder imprimir dentro del pdf
from reportlab.pdfgen import canvas
#para poder importar la fecha actual
from datetime import datetime


#Definimos el menu de nuestro proyecto
def menu():
    #mientras sea verdad
    while True:

        #Menú que imprimiremos
        print('\n'
              '\t\t\t\t\033[1mAPLICACIÓN ESTEGANOCR\033[0m\n\n'
              '\t\t1) Insertar mensaje oculto en una imagen.\n'
              '\t\t2) Extraer mensaje oculto de una imagen.\n'
              '\t\t3) Convertir la imagen a escala de grises.\n'
              '\t\t4) Extraer cadena visible en una imagen.\n'
              '\t\t5) Informe de las extracciones (PDF).\n'
              '\t\t6) Salir.'
        )
        #Pedimos al usuario que elija una opción
        opcion = input('\t\tOpción: ')
        #si es uno
        if opcion == '1':
            # Título
            print("\n\t\t \033[1mOPCIÓN: Insertar mensaje oculto en una imagen\033[0m")
            oculta=texto_oculto()
        #si es dos
        elif opcion == '2':
            # Título
            print("\n\t\t \033[1mOPCIÓN: Extraer mensaje oculto de una imagen\033[0m")
            extraer_oculto(oculta)
        #si es tres
        elif opcion == '3':
            # Título
            print("\n\t\t \033[1mOPCIÓN:  Convertir la imagen a escala de grises\033[0m")
            escala_gris()
        elif opcion == '4':
            # Título
            print("\n\t\t \033[1mOPCIÓN:  Extraer cadena visible en una imagen\033[0m")
            extraer_cadena()
        elif opcion == '5':
            # Título
            print("\n\t\t \033[1mOPCIÓN: Informe de las extracciones (PDF)\033[0m")
            extr_pdf()
        elif opcion == '6':
            print('\n\t\tSaliendo...')
            #en esta opción sale del menu y termina el programa
            break
        else:
            print('\n\t\tSólo se aceptan número incluidos dentro del menú\n')





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
    print(f'\n\t\t{original} tiene {str(wid)} de ancho y de {str(hgt)} alto')
    #Mostramos la imágen en una ventana emergente
    cv2.imshow('Imagen original', img_ori)
    #El waitKey nos permite mantener la imagen hasta que cerremos la ventana
    cv2.waitKey(0)
    #Pedimos al usuario que ponga el mensaje secreto que desee ocultar en la imagen
    men_secreto = input('\n\t\tIntroduzca el mensaje de texto a ocultar: ')
    #guardamos el mensaje secreto
    secret = lsb.hide(original, men_secreto).save(oculta)
    #e indicamos que estamos insertandolo
    print('\n\t\tInsertando texto en la imagen...')
    #Para poder comparar los bytes de la imagenes usamos el método open importado de la libreria Image de PIL
    # lo hacemos con la imagen original y con la imagen que tiene el mensaje oculto
    ori_img = Image.open(original)
    ocul_img = Image.open(oculta)
    #Si la original es distinta a la de la imagen oculta entonces
    if ori_img != ocul_img:
        #Leemos la imagen que oculta el texto con cv2 e indicamos que el fichero es distinto
        img_oculta = cv2.imread(oculta)
        print(f'\n\t\tEl fichero {original} es diferente a {oculta}')
        #Para poder mostrarla por la ventana emergente
        cv2.imshow('Con texto oculto', img_oculta)
        #Le pedimos que espere hasta que nosotros la cerremos
        cv2.waitKey(0)
    #devolvemos la imagen obtenida para usarla en la segunda opción
    return oculta


def extraer_oculto(oculta):

    #la imagen con el texto oculto anterior lo traemos
    print(f'\n\t\tEl fichero de la imagen con texto oculto se llama: {oculta}')
    #revelamos su secreto y lo imprimimos
    m_secret = lsb.reveal(oculta)
    print('\n\t\tExrayendo el texto de la imagen...')
    print(f'\n\t\tEl texto oculto es: {m_secret}')
    #por último guardamos el secreto en un fihero llamado extracción.txt
    with open('extraccion.txt', 'w+') as secreto:
        secreto.writelines(f'-> Extracción del Texto Oculto\n'
                           f'{m_secret}.')


def escala_gris():
    #tenemos la imagen original
    original = 'proyimag1T.png'
    #Y la variable donde crearemos nuestra copia en grises
    imggris = 'proyimgr1T.png'
    #imprimimos
    print(f"\n\t\tEl fichero de la imagen se llama: {original}")
    print("\n\t\tConvirtiendo la imagen a escala de grises...")
    # abrimos la imagen
    imag_gris = cv2.imread(original)
    # la convertimos a grises
    gris = cv2.cvtColor(imag_gris, cv2.COLOR_BGR2GRAY)
    #la abrimos
    cv2.imshow('Escala de grises', gris)
    cv2.waitKey(0)
    # la guardamos en proyimgr1T.png
    grises = cv2.imwrite(imggris, gris)
    #Imprimimos donde esta guardado
    print(f"\n\t\tEl fichero de la imagen en grises: {imggris}")

def extraer_cadena():
    #declaramos la imagen
    imagen = 'imagtext1T.png'
    print(f'\n\t\tEl fichero de la imagen se llama: {imagen}')
    #la abrimos
    img_abierta = Image.open(imagen)
    print('\n\t\tExtrayendo el texto de la imagen...')
    #le decimos al programa de donde esta nuestra funciona de extracción y que la ejecute
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.tesseract_cmd = path_to_tesseract
    #pasamos la ejecución a una variable
    text = pytesseract.image_to_string(img_abierta)[:-5]#le ponemos esto porque a la imagen le sobra espacios
    print(f'\n\t\tEl texto recuperado es: {text}.')
    with open('extraccion.txt', 'a+') as secreto:
        secreto.writelines(f'\n-> Extracción del Texto estampado en la imagen'
                           f'\n{text}.')

def extr_pdf():

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
    #Creamos una variable que sera donde empieze el texto de extraccion.txt
    y = 500
    # y2= 370
    #recorremos palabra por palabras hasta los saltos creando lineas
    for line in extrac.split('\n'):
        #le damos tamaño y fuente a la letra
        c.setFont("Helvetica", 12)
        # dibujamos todas las lineas del documento en el pdf
        c.drawString(65, y, line)
        # con cada vuelta imprime 13 pixeles más abajo
        y = y - 13
        #si las lineas empiezan por -> ignorar
        if not line.startswith('->'):
            #añadimos a la lista las dos frases que necesitamos y las separamos en una variable
            cadenas.append(line)
            # c.drawString(65, y2, f"El texto oculto consta de {str(len(line))} caracteres")
            # y2 = y2-20

    # Extracciones de la cuenta de caracteres y palabras de ambos textos con la variable en donde se encuentran
    # Ponemos en una variable la fecha del sistema
    fecha = datetime.now()
    # declaramos el tamaño y la fuente de letra que usaremos
    c.setFont('Helvetica', 12)
    #definimos de donde sale la primera frase
    #imprimimos primero la fecha
    c.drawString(65, 400, f"Las extracciones se realiaron el {fecha.date()}.")
    #imprimimos la cantidad de caracteres del texto oculto
    c.drawString(65, 370, f"El texto oculto consta de {len(cadenas[0][:-1])} caracteres.")
    # imprimimos la cantidad de caracteres del texto estampado
    c.drawString(65, 350, f"El texto estampado consta de {len(cadenas[1][:-1])} caracteres.")
    # imprimimos la cantidad de palabras del texto oculto
    c.drawString(65, 330, f"El texto oculto está compuesto de {len(cadenas[0].split())} palabras.")
    # imprimimos la cantidad de palabras del texto estampado
    c.drawString(65, 310, f"El texto estampado está compuesto de {len(cadenas[1].split())} palabras.")
    # pie de página
    c.setFont('Helvetica', 12)
    # Imprimimos el pie de página
    c.drawString(500, 50, 'Page#1')
    # paara poder ver la página
    c.showPage()
    # Salva la página
    c.save()


if __name__ == "__main__":
    menu()