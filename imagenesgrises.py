import cv2 as cv2

original = 'proyimag1T.png'
oculta = 'proyimod1T.png'

print("OPCIÓN: Convertir la imagen a escala de grises")
print("El fichero de la imagen se llama: proyimag1T.png")
print("Convirtiendo la imagen a escala de grises...")
imag_gris=cv2.imread(original)
gris=cv2.cvtColor(imag_gris, cv2.COLOR_BGR2GRAY)

cv2.imshow('imag_gris',gris)
cv2.waitKey(0)
print("El fichero de la imagen en grises: proyimgr1T.png")
