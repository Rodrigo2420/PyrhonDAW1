def main():
    trimestre = {}
    for i in range(5):
        alumno = input("Introduce el nombre del alumno :")
        nota_alumno = input("Introduce la nota del alumno :")
        trimestre[alumno] = nota_alumno
    
    print(trimestre)    
    
main()