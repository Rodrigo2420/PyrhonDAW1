def main():
    cont = 0
    val_enteros = []
    for i in range (10):
        val_enteros.append(int(input("Introduce un numero :")))
    
    for i in range (len(val_enteros)):
        if val_enteros[i] > 100:
            cont += 1
        
        
    print(cont)
    
main()