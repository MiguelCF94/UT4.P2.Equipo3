import random
import re

def main(): 
    comprueba(generar())
    
def generar():
    numString=list()
    lista=list()
    
    for i in range(0,4):
        aleatorio=random.randint(0, 9)
        while aleatorio in lista:
            aleatorio=random.randint(0, 9)
        lista.append(aleatorio)    
    
    for i in range(0,len(lista),1):
        numString+=str(lista[i])    
        
    print(numString)
    return numString   


def comprueba(num):
    listaEntrada=list()
    listaMuertos=list()
    listaHeridos=list()
        
    while True: 
        numEntrada=input("Introduce numero ")
        
        while re.match("/^[0-9]{4}$/", numEntrada)==None:
            numEntrada=input("Introduce un numero valido ")
            
        for i in range(0,4):
            listaEntrada.append(numEntrada[i])
        
        if num==listaEntrada:
            print("Acertado")
            return 
            
        else:
            for i in range(0,4):
                if num[i]==listaEntrada[i] and listaEntrada[i] not in listaMuertos:
                    listaMuertos.append(listaEntrada[i])
                elif listaEntrada[i] in num and listaEntrada[i] not in listaHeridos:
                    listaHeridos.append(listaEntrada[i])
            
            print("Muertos:")
            for i in range(len(listaMuertos)):
                print(listaMuertos[i])
            
            print("Heridos:")
            for i in range(len(listaHeridos)):   
                print(listaHeridos[i])
                
        listaEntrada.clear()  
        numEntrada=(input("Introduce numero "))
    

if __name__ == '__main__':
    main()