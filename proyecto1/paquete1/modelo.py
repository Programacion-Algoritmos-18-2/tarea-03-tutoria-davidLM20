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

	def presentar_datos(self):
		cadena = "%s\n\t%s" % (self.obtener_nombres(), self.obtener_ciudad())
		return cadena
#se crea clase 
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

	def presentar_datos(self):
		cadena = "Estudiante: %s\n" % (self.obtener_nombres())
		cadena = "%s %s\n" % (cadena,"lista_docentes")
		for x in range(0, len(self.docentes)):
			cadena = "%s\n\t-%s|%s" %(cadena, self.docentes[x].obtener_nombres(), self.docentes[x].obtener_ciudad())
		return cadena		