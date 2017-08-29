#Python usa librerias como matplotlib con objetos predeterminados como pyplot que tienen propiedades que permiten enviar las instrucciones a la maquina de una forma resumida. Matplotlib es una libreria para crear graficas en 2 dimensiones. 
import matplotlib.pyplot as plt
#Construimos el objeto plt introduciendo valores que se grafican contra el numero de entrada. Por ejemplo si queremos graficar el crecimiento de un material por dia en centimetros. 
plt.plot([3,3,4,5,6,7,8,8,8,10,11,12,12,12,13,14,15,16,17,18,19])
#Con esta isntruccion colocamos un titulo al eje Y de la grafica. 
plt.ylabel('Hermanos y primos por edad[años]')
#Con esta isntruccion guardamos la imagen con el formato que queramos.
plt.savefig('temp.png')
#Con esta instruccion mostramos la figura. 
plt.show()


