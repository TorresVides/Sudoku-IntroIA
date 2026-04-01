########################################################################################################
#	Intro IA Proyecto2, TableroSudoku
#	Estudiante Karol Torres
#	Este fichero se encarga de representar el Sudoku a través de una matriz
########################################################################################################

class TableroSudoku:	
	def __init__(self): #Inicializar el objeto TableroSudoku con una matriz y celdas_fijas
		self.matriz = []
		self.celdas_fijas = set()

	def guardar_tablero(self): # Lee el .txt y lo guarda
		matriz = []
		celdas_fijas = set()

		with open("sudoku.txt", "r") as sudoku:
		
			for i, linea in enumerate(sudoku):
				linea = linea.strip()

				if linea:
					fila = [int(x) for x in linea.split(",") if x != ""]
					matriz.append(fila)


					for j, valor in enumerate(fila):
						if valor != 0:
							celdas_fijas.add((i, j))

		self.matriz = matriz
		self.celdas_fijas = celdas_fijas
	

	def consultar_tablero(self):
		return [fila[:] for fila in self.matriz] # Devuelve una copia del estado actual

	def buscar_vacia(self):
		for fila in range(len(self.matriz)):
			for columna in range(len(self.matriz[fila])):
				if self.matriz[fila][columna] == 0:
					return (fila, columna)
				
		return None

	def modificar_celda(self,fila,col,valor):
		if (fila, col) not in self.celdas_fijas:
			self.matriz[fila][col] = valor
			return True
		return False

	def limpiar_celda(self, fila, col):
		if(fila, col) not in self.celdas_fijas:
			self.matriz[fila][col] = 0
			return True
		return False

	def esta_completo(self):
		vacias = self.buscar_vacia()
		if vacias == None:
			return True
		return False

	def obtener_fila(self, indice):
		if indice >= len(self.matriz) or indice < 0:
			print("Indice de fila invalido")
			return None
		return self.matriz[indice]		
				

	def obtener_col(self, indice):
		if indice >= len(self.matriz[0]) or indice < 0:
			print("Indice de columna invalido")
			return None
		columna = []
		for fila in range(len(self.matriz)):
			columna.append(self.matriz[fila][indice])

		return columna

	# Devuelve el bloque al que pertenece la celda en la posicion (fila, col)
	def obtener_3x3(self, fila, col):
		fila_inicio = fila - (fila%3)
		col_inicio = col - (col%3)

		_3x3 = []

		for i in range(fila_inicio , fila_inicio + 3):
			for j in range(col_inicio , col_inicio + 3):
				
				_3x3.append(self.matriz[i][j])

		return _3x3
		
