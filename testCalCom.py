import unittest
import calculadoraComplejos


class TestStringMethods(unittest.TestCase):
##        print(calculadoraComplejos.sumar([3,2],[-1,2]))
    def test_deberiaSumarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.sumar([3,2],[-1,2]),(2,4))


    def test_deberiaRestarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.restar([3,2],[-1,2]),(4,0))

        
    def test_deberiaMultiplicarNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.multiplicar([3,2],[-1,2]),(-7,4))

        
    def test_deberiaDividirNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.divicion([3,2],[-1,2]),(0.2,-1.6))

    def test_deberiaHacerModuloNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.modulo([3,2]),(3.605551275463989))

    def test_deberiaHacerConjugadoNumerosComplejos(self):
        self.assertEqual(calculadoraComplejos.conjugado([3,2]),(3,-2))
    def test_deberiaHacerCartesianasPolares(self):
        self.assertEqual(calculadoraComplejos.cartesianasPolares([1,(3**0.5)]),(1.9999999999999998,59.99999999999999))
        
if __name__== '__main__':
    unittest.main()
    
