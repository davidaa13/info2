class paciente():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def asigNombre(self,nombre):
        self.__nombre = nombre
    def asigcedula(self,cedula):
        self.__cedula = cedula
    def asigenero(self,genero):
        self.__genero = genero
    def asigservicios(self,servicio):
        self.__servicio = servicio

    def vernombre(self):
        return self.__nombre
    def vercedula(self):
        return self.__cedula
    def vergenero(self ):
        return self.__genero
    def verservicio(self):
        return self.__servicio

class sistema:
    def __init__(self):
        self.__listapacientes = []
        self.__numpacientes = len(self.__listapacientes)

    def IngresarPac(self):
        nombre = input("Ingresar el nombre")
        cedula = input("Ingresar la cedula")
        genero = input("Ingresar el genero")
        servicio = input("Ingresar el servicio")

        p = paciente()
        p.asigNombre(nombre)
        p.asigcedula(cedula)
        p.asigenero(genero)
        p.asigservicios(servicio)

        self.__listapacientes.append(p)
        self.__numpacientes = len(self.__listapacientes)

    def vernumpacientes(self):
        return self.__numpacientes
    
    def verDatPacientes(self):
        cedula = int(input("Ingrese la cedula a buscar:"))
        for paciente in self.__listapacientes:
            if cedula == paciente.vercedula():
                print("Nombre:" + paciente.vernombre())
                print("Cedula:" + str(paciente.vercedula()))
                print("Género:" + paciente.vergenero())
                print("Servicio:" + paciente.verservicio())

miSistema = sistema()

while True:
    opcion = int(input("1. Nuevo Paciente - 2. Numero de pacientes - 3. Datos de paciente - 4. Salir "))
    if opcion == 1:
        miSistema.IngresarPac()
    elif opcion == 2:
        print("Ahora hay: " + str(miSistema.vernumpacientes()))
    elif opcion == 3:
        miSistema.verDatPacientes()
    elif opcion == 4:
        break
    else:
        print("Opcion no valida")