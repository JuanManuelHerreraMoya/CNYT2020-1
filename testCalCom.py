import unittest
import calculadoraComplejos


class TestStringMethods(unittest.TestCase):

    def test_deberiaSumarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.sumar([3,2],[-1,2]),([2,4]))


    def test_deberiaRestarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.restar([3,2],[-1,2]),([4,0]))

        
    def test_deberiaMultiplicarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.multiplicar([3,2],[-1,2]),([-7,4]))

        
    def test_deberiaDividirNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.divicion([3,2],[-1,2]),((0.2,-1.6)))

    def test_deberiaHacerModuloNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.modulo([3,2]),(3.605551275463989))

    def test_deberiaHacerConjugadoNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.conjugado([3,2]),((3,-2)))
        
    def test_deberiaHacerCartesianasPolares(self):
        self.assertEqual(calculadoraComplejos.cartesianasPolares([3,2]),(3.605551275463989, 33.690067525979785))
        
    def test_deberiaSumarVectores(self):
        print(calculadoraComplejos.sumaVectores([[5,0],[2,0]],[[2,0],[8,0]]))
        self.assertEqual(calculadoraComplejos.sumaVectores([[5,0],[2,0]],[[2,0],[8,0]]),([17, 0]))

    def test_DeberiaMultiplicaREscalar_Vectores(self):
       self.assertEqual(calculadoraComplejos.escalarPorVector(3,[[2,1], [1,-3]]),([[6, 3], [3, -9]]))

    def test_DeberiaHacerinversa_Vectores(self):
       self.assertEqual(calculadoraComplejos.inversaVectores([[2,1], [1,-3]]),([(-2, -1), (-1, 3)]))

    def test_adicion_Matrices_Complejos(self):
       self.assertEqual(calculadoraComplejos.adicionMat([[[1,-1],[2,7]] , [[4,0],[5,1]]] , [[[2, 0],[5,0]] , [[3,0],[7,0]]]),([[7, 0], [12, 1]]))
       
    def test_multiplicacion_Escalar_Matrices(self):
       self.assertEqual(calculadoraComplejos.escalarPorMatriz(2,[[[1,0],[2,0]],[[4,0],[5,0]]]),([[[2, 0], [4, 0], [8, 0], [10, 0]]]))
  
    
    def test_matriz_Transpuesta(self):
      resu = calculadoraComplejos.matrizTranspuesta([[[1,0],[2,0],[3,0]] , [[4,0],[5,0],[7,0]]])
      self.assertEqual(resu,([[[1, 1], [2, -7], [3, -4]], [[4, 0], [5, -10], [7, 4]], [[1, 0], [4, 0]], [[2, 0], [5, 0]], [[3, 0], [7, 0]]]))

    def test_matriz_Conjugada(self):
      self.assertEqual(calculadoraComplejos.matrizConjugada([[[1,-1],[2,7],[3,4]] , [[4,0],[5,10],[7,-4]]]),([[[1, 1], [2, -7], [3, -4]],[[4, 0], [5, -10], [7, 4]]]))

    def test_producto_Tensor_Vectores(self):
      self.assertEqual(calculadoraComplejos.productoTensorVectores([[2,1], [1,-3]],[[5,0],[2,0]]),([[10, 5], [4, 2], [5, -15], [2, -6]]))

    def test_producto_Tensor_Matrices(self):
        res = calculadoraComplejos.productoTensorMatriz([[[1,-1],[2,7]] , [[4,0],[5,1]]],[[[2, 0],[5,0]] , [[3,0],[7,0]]])        
        self.assertEqual(res,([[[2,-2],[5,-5],[4,14],[10,35]],[[3,-3],[7,-7],[6,21],[14,49]],[[8,0],[20,0],[10,2],[25,5]],[[12,0],[28,0],[15,3],[35,7]]]))
                       
    def test_multi_matrices(self) :
      self.assertEqual(calculadoraComplejos.multiMatriz([[[1,-1],[2,7]] , [[4,0],[5,1]]],[[[2, 0],[5,0]] , [[3,0],[7,0]]]),[[[8, 19], [19, 44]], [[23, 3], [55, 7]]])


    def test_producto_interno(self):
      self.assertEqual(calculadoraComplejos.productoInternoVectores([[2,1], [1,-3]],[[5,0],[2,0]]),([2, -6]))

    def test_distancia_Vectores(self):
      self.assertEqual(calculadoraComplejos.distanciaVectores([[2,1], [1,2]],[[5,0],[2,0]]),([2.23606797749979, -10]))

if __name__== '__main__':
    unittest.main()
    
