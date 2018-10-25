#se crea las clasas docente
class Docente:

	def __init__(self,n,a):
		self.nombres = n
		self.ciudad = a
	# metodos para obtener y agregar nombre
	def agregar_nombre(self,n):
		self.nombres = n

	def obtener_nombres(self):
		return self.nombres

	#metodos para obtener y agregar ciudad	
	def agregar_ciudad(self,a):
		self.ciudad = a

	def obtener_ciudad(self):
		return self.ciudad

	#se crea el metodo para obtener la presentacion de datos 
	def presentar_datos(self):
		cadena = "%s\n\t%s" % (self.obtener_nombres(), self.obtener_ciudad())
		return cadena
#se crea clase estudiante
class Estudiante:
	def __init__(self,n,lista_docentes):
		self.nombres = n
		self.docentes = lista_docentes
	
	# metodos para obtener y agregar nombre
	def agregar_nombre(self,n):
		self.nombres = n

	def obtener_nombres(self):
		return self.nombres
    
    #metodos para obtener y agregar docentes
	def agregar_docentes(self,lista_docentes):
		self.docentes = lista_docentes

	def obtener_docentes(self):
		return self.docentes
    
    #se crea metodo para la presentacion de datos
	def presentar_datos(self):
		cadena = "Estudiante:%s\n" % (self.obtener_nombres())
		cadena = "%s%s\n" % (cadena,"Lista_docentes")#se concatena la primera cadena a una nueva que tenga el encabezado de las listas
		#se recorre cada valor de la lista que devuelbe docentes
		for x in self.obtener_docentes():
			cadena = "%s %s:\n " %(cadena, x.presentar_datos()) #se concatena a la cadena la lista que retorna docentes
		return cadena		