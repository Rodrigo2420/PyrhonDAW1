'''Desarrollar un programa que permita almacenar los datos de n alumnos. Definir un diccionario
cuya clave será el número de alumno en el centro. Como valor almacenar una lista con el nombre, la
materia a la que está apuntado y la nota obtenida en dicha materia. Un alumno puede estar apuntado
a diferentes materias. Implementar funciones para cargar los datos de los alumnos, listar todos los
alumnos y consultar un alumno a través de su id. Una posible ejecución es:
'''
def cargar_datos(alumnos): 
    materias = {}
    id = int(input("Introduce el id del alumno en el centro :"))
    nombre = input("Introduce el nombre del alumno : ")
    j = int(input("Introduce el numero de materias que tiene el alumno :"))
    for i in range (j):
        materia = input("Introduce el nombre de la materia")
        nota = float(input("Introduce la nota del alumno en la materia introducida :"))
        materias[materia] = nota
    lista = [nombre,materias]
    alumnos[id]=lista    
   
    
def listar_alumnos(alumnos):
    for k,v in alumnos.items():
        print(f"ID : {k} \nDATOS :\n {v}")


def buscar_alumno(ID,alumnos):
    if ID in alumnos.keys():
        print(f"Alumno encontrado {alumnos[ID]}")
    else:
        print(f"el alumno con id : {ID} no se encuentra en nuestra base de datos")
        
        
def main():
    alumnos = {}
    salir = False
    while not salir:
        opci = int(input("\nSeleccione una opcion : \n1. cargar los datos de alumno\n2.Listar todos los alumnos\n3.Consulatar alumno por id\n4.Salir "))
        match (opci):
            case 1:
                cargar_datos(alumnos)
            case 2:
                listar_alumnos(alumnos)
            case 3:
                ID = int(input("Introduce el id del alumno que quieras buscar :"))
                buscar_alumno(ID,alumnos)
            case 4:
                salir = True
            case _:
                print("Opcion no valida")
    
    print("Saliendo.....................")
    
    
main()
    
