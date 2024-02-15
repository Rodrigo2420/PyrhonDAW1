def main():
    numeros = []
    numeros_aux = []
    for i in range (1,5):
        numeros_aux = []
        for j  in range (i):
            numeros_aux.append(j+1)
        numeros.append(numeros_aux)
        
    print(numeros)
    
main()
        
        