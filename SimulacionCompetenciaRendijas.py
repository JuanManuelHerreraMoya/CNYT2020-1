import calculadoraComplejos as calculadora


MatrizPrueba = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
      [(1/(2**0.5),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
      [(1/(2**0.5),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],
      [(0,0),((-1/(6**0.5)),(1/(6**0.5))),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],
      [(0,0),((-1/(6**0.5)),(-1/(6**0.5))),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],
      [(0,0),((1/(6**0.5),-1/(6**0.5))),((-1/(6**0.5),1/(6**0.5))),(0,0),(0,0),(1,0),(0,0),(0,0)],
      [(0,0),(0,0),(-1/(6**0.5),-1/(6**0.5)),(0,0),(0,0),(0,0),(1,0),(0,0)],
      [(0,0),(0,0),(1/(6**0.5),-1/(6**0.5)),(0,0),(0,0),(0,0),(1,0),(0,0)]]





ListaElementos = [[(1,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)],[(0,0)]]
vecesPorHacer = 2
def main():
   simulacion(MatrizPrueba,ListaElementos,vecesPorHacer)

def simulacion(MatrizPrueba,ListaElementos,vecesPorHacer):
   for i in range(vecesPorHacer):
      resu = calculadora.multiMatriz(MatrizPrueba,ListaElementos)
   print(resu)
main()
