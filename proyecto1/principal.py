#se importa los metodos del paquete 1
from paquete1.modelo import *
#se crea los objetos 
d = Docente("Docente: B.D", "Loja")
d2 = Docente("Docente: Pray", "Quito")
#se crea la lista 
listado = [d,d2]
e = Estudiante("Luis", listado)
#se instancia el metodo para presentar 
print(e.presentar_datos())
