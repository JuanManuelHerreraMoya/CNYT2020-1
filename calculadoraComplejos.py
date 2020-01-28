import math 

num1 = [1,-3]
num2 = [2,0]


vector1 =[[6, -4], [7, 3], [4.2, -8.1], [0, -3]]
vector2 =[[16, 2.3], [0, -7], [6, 0], [0, -4]]
vectorFinal = []


matriz1 = [[[1,2],[3,4]] , [[5,6],[7,8]]]# , [[9,10],[11,12]]]
matriz2 = [[[3,-5],[4,0]] , [[0,0],[0,0]]]
matrizFinal = []

c = [0,0]
def sumar(num1,num2):
    resuE = (num1[0])+(num2[0])
    resuI = (num1[1])+(num2[1])
    c[0],c[1] = resuE,resuI
    return (resuE,resuI)

def restar(num1,num2):
    resuE = (num1[0])-(num2[0])
    resuI = (num1[1])-(num2[1])
    c[0],c[1] = resuE,resuI
    return (resuE,resuI)

def multiplicar(num1,num2):
    
    res1 = num1[0]*num2[0] 
    res2 = num1[0]*num2[1]
    res3 = num1[1]*num2[0]
    res4 = (num1[1]*num2[1])*-1
    res1 = res1+res4
    res2 = res2+res3
    c[0],c[1] = res1,res2
    return (res1,res2)

def divicion(num1,num2):
    aux = num2[:]
    aux[-1]=aux[-1]*-1
    conjugado1=multiplicar(num1,aux)
    conjugado2=multiplicar(num2,aux)
    res1 = conjugado1[0]/conjugado2[0]
    res2 = conjugado1[1]/conjugado2[0]
    c[0],c[1]=res1,res2
    return (res1,res2)


def modulo(num1):
    resu = ((num1[0]**2)+(num1[1]**2))**0.5
    c[0],c[1]=resu,"null"
    return resu
def inversa(num1):
    c[0],c[1]= num1[0]*-1,num1[1]*-1
    return  c[0],c[1]
def conjugado(num1):
    c[0],c[1]=num1[0],(num1[1]*-1)
    return (c[0],c[1])

def cartesianasPolares(num1):
    hipo = ((num1[0]**2)+num1[1]**2)**(0.5)
    angulo = math.degrees(math.atan(num1[1]/num1[0]))

    if num1[0]<0 and num1[1]<0:
        angulo = angulo + 180
    elif 0>num1[1]:
        angulo = 360 -angulo
    elif 0>num1[0]:
        angulo = 180- angulo
    c[0],c[1]= hipo ,angulo
    return (hipo,angulo)


def sumaVectores(vec1,vec2):
    if len(vec1)== len(vec2):
        for i in range(len(vec1)):
            vectorFinal.append(sumar(vec1[i],vec2[i]))
    return vectorFinal



def inversaVectores(vec1):
    for i in range(len(vec1)):
        vectorFinal.append(inversa(vec1[i]))
    return vectorFinal

##
##def adicionMat(mat1,mat2):
##    for i in range(len(mat1)):
##        aux = []
##        for j in range(len(mat1[0])):
##            


def matrizTranspuesta(mat1):
    for i in range(len(mat1[0])):
        temporal = []
##        print((mat1[0]))
        for j in range(len(mat1)):
            temporal.append(mat1[j][i])
        matrizFinal.append(temporal)
    return matrizFinal
    
def matrizConjugada(mat1):
    resu = ""
    for i in range(len(mat1)):
        temporal = []

        for j in range(len(mat1[0])):
            temporalNumeros = []
            resu= (conjugado(mat1[i][j]))
            temporalNumeros.append(resu[0])
            temporalNumeros.append(resu[1])
            temporal.append(temporalNumeros)
        matrizFinal.append(temporal)
def prettyPrinting(c):
    if c[1]!="null":
        if c[1]>=0:
            print (str(c[0])+"+"+str(c[1])+"i")
        else:
            print (str(c[0])+""+str(c[1])+"i")
    else:
        print(str(c[0]))

        


def prettyprintingVectores(vf):
    vectorPintar = []
    if vectorFinal == [""]:
        print("No se pudo Sumar vector , Longitudes diferentes")
    else:
        for i in vf:
            if (i[1]>0):
                print(str(i[0])+"+"+str(i[1])+"i")
            else:
                print(str(i[0])+str(i[1])+"i")

                
    
def prettyprintingMatriz(matrizFinal):
    for i in matrizFinal:
        print(*i)


        

def main():
##    matrizConjugada(matriz1)
    matrizTranspuesta(matriz1)
##    inversaVectores(vector1)
##    sumaVectores(vector1,vector2)
##    cartesianasPolares(num1)
##    multiplicar(num1,num2)
##    sumar(num1,num2)
##    restar(num1,num2)
##    divicion(num1,num2)
##    modulo(num1)
##    conjugado(num1)
##    prettyPrinting(c)
##    prettyprintingVectores(vectorFinal)
    prettyprintingMatriz(matrizFinal)
main()
