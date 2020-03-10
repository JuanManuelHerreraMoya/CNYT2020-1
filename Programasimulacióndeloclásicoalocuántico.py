import calculadoraComplejos as calculadora


matriz = [[[0,0],[0,0],[0,0],[0,0],[0,0],[1,0]],[[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[1,0],[0,0],[0,0]],[[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0],[1,0],[0,0]],[[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]]]
estadoInicial = [[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[1,0]]]
repeticiones = 2019


def canicas(matriz,estaodInicial,repeticiones):
   total = 0
   
   while repeticiones>0:
      estaodInicial = calculadora.multiMatriz(matriz,estadoInicial)

      repeticiones -=1
      print(estaodInicial)
   return estadoInicial

def main():
   canicas(matriz,estadoInicial,repeticiones)
main()
