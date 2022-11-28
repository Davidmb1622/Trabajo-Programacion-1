import cv2 as cv2

original = 'proyimag1T.png'

print("\nOPCIÓN: Convertir la imagen a escala de grises")
print(f"\nEl fichero de la imagen se llama: {original}")
print("\nConvirtiendo la imagen a escala de grises...")
#abrimos la imagen
imag_gris = cv2.imread(original)
#la convertimos a grises
gris = cv2.cvtColor(imag_gris, cv2.COLOR_BGR2GRAY)
#la guardamos en proyimgr1T.png
cv2.imshow('Escala de grises',gris)
cv2.waitKey(0)

grises = cv2.imwrite('proyimgr1T.png', gris)
cv2.imshow('Escala de grises',grises)
cv2.waitKey(0)


print(f"El fichero de la imagen en grises: proyimgr1T.png")
#El guardado de imagen era muy complicado y es mejor hacerlo mas sencillo y que no de errores