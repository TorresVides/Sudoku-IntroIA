##############################################################################
#       Intro IA Proyecto2, Interfaz
#       Estudiante Karol Torres
#       Este fichero coordina la interacción con el usuario
##############################################################################
from tableroSudoku import TableroSudoku

class Interfaz:
    def __init__(self):
        self.tablero = TableroSudoku()
        self.solucionador = None

    def imprimir_tablero(self):
        matriz = self.tablero.consultar_tablero()

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")

                valor = matriz[i][j]
                if valor == 0:
                    print(".", end=" ")
                else:
                    print(valor, end=" ")

            print()
        
    def menu(self):
        print("\nMetodos de resolucion:")
        print("1. Fuerza bruta")
        print("2. Backtraking")
        print("3. Backtraking y Comprobacion hacia Delante")

    def seleccionar_metodo(self, opcion):
	    if opcion == "1":
		    print ("Resolver por fuerza bruta")
            self.solucionador = "FB"
	    elif opcion == "2":
		    print ("Resolver por backtraking")
            self.solucionador = "BT"
	    elif opcion == "3":
		    print ("Resolver con backtraking y comprobación hacia delante")
            self.solucionador = "CD"
	    else:
		    print ("Opcion invalida")
            self.solucionador = None

       

    def iniciar(self):
        self.tablero.guardar_tablero()
        
        print("Tablero cargado:\n")
        self.imprimir_tablero()

        self.menu()
        opcion = input("\nSeleccione el metodo para resolver el sudoku")
        self.seleccionar_metodo(opcion)

        opcion = input("Seleccione un método para resolver el sudoku: ")
        self.seleccionar_metodo(opcion)

        if self.solucionador is not None:
            pritn("\nInterfaz lista para conectar el solucionador!")
            return True

        return False

    interfaz = Interfaz()
    interfaz.iniciar()

