#funciones....
from reportlab.pdfgen import canvas
from FuncionQR import *
ruta="C:/Users/Aula 25/Desktop/Modularidad python/Prueba funciones/"
nombreArchivo=ruta+"reporteGlobal.pdf"
nombreQR = ruta + "miQR.png"

def generarPDF(listaNombre,listaEdades):
    generarQR(nombreQR,"hola desde la funcion")
    c= canvas.Canvas(nombreArchivo)
    xInicial =200
    yInicial = 700
    c.drawString(xInicial,yInicial,"Edad")
    c.drawString(xInicial+120,yInicial,"Nombre")

    c.drawImage(nombreQR,200,400,100,100)
    for i in range(len(listaNombre)):
        yInicial = yInicial -20
        c.drawString(xInicial,yInicial,listaEdades[i])
        c.drawString(xInicial+120,yInicial,listaNombre[i])
    c.save()
    print("-------Reporte generado--------")