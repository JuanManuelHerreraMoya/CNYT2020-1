import calculadoraComplejos 
##import matplotlib.pyplot as plt

def canicas(MatrizPrueba,vecesPorHacer,numRendijas):
   for i in range(numRendijas):
      vecesPorHacer = calculadoraComplejos.multiMatriz(MatrizPrueba,vecesPorHacer)
   return vecesPorHacer
def probabilistico_mas_de_dos_rendijas(MatrizPrueba,vecesPorHacer,numRendijas,target):
   if len(MatrizPrueba) != target:
      print("Hay un error entre el taget y la matriz")
   else:
      for i in range(numRendijas):
         vecesPorHacer = calculadoraComplejos.multiMatriz(MatrizPrueba,vecesPorHacer)
   return vecesPorHacer
def  cuantico_de_rendijas(MatrizPrueba,vecesPorHacer,numRendijas,target):
   if len(MatrizPrueba) != target:
      print("Hay un error entre el taget y la matriz")
   else:
      for i in range(numRendijas):
         vecesPorHacer = calculadoraComplejos.multiMatriz(MatrizPrueba,vecesPorHacer)
   return vecesPorHacer

def main():
   
   print() 
main()
