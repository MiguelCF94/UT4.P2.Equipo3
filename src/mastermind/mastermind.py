import random
import re

def main(): 
    comprueba(generar())
    
def generar():
    numString=list()
    lista=list()
    
    #Genera números aleatorios y los introduce en la lista
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
    
    numEntrada=str(input("Introduce número "))
        
    while True: 
        
        #Comprueba la entrada del usuario y compara con la regex. Si devuelve None, sigue
        #pidiendo una entrada
        while re.match("^[0-9]{4}$", numEntrada)==None:
            print("Introduce un número de cuatro cifras")
            numEntrada=input()
        
        #Añade a una lista la entrada del usuario
        for i in range(0,4):
            listaEntrada.append(numEntrada[i])
        
        #Si acierta, finaliza el juego
        if num==listaEntrada:
            print("Acertado")
            return 
            
        else:
            #Comprueba que un número de la lista de los muertos no está en la de los heridos
            #y viceversa
            for i in range(0,4):
                if num[i]==listaEntrada[i] and listaEntrada[i] not in listaMuertos:
                    listaMuertos.append(listaEntrada[i])
                elif listaEntrada[i] in num and listaEntrada[i] not in listaHeridos:
                    listaHeridos.append(listaEntrada[i])
                    
            #Va recorriendo las listas de heridos y muertos y borra de la lista correspondiente
            #el número repetido de la otra lista
            for i in range(len(listaMuertos)):        
                if listaMuertos[i] in listaHeridos:
                    del listaHeridos[i]
                    
            for i in range(len(listaHeridos)):
                if listaHeridos[i] in listaMuertos:
                    del listaMuertos[i]
            
            #Muestra muertos y heridos
            print("Muertos:")
            for i in range(len(listaMuertos)):
                print(listaMuertos[i])
            
            print("Heridos:")
            for i in range(len(listaHeridos)):   
                print(listaHeridos[i])
            
            listaMuertos.clear()
            listaHeridos.clear()
        
        #Reinicia la entrada del usuario y pide nueva entrada
        listaEntrada.clear()  
        numEntrada=(input("Introduce número "))
    

if __name__ == '__main__':
    main()
