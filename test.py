import unittest

from main import generar_numero_secreto, turno_jugadora

class TestJuego(unittest.TestCase):

    def test_generar_numero_secreto(self):
        # Prueba para asegurar que el número secreto está entre 1 y 100
        numero_secreto = generar_numero_secreto()
        self.assertTrue(1 <= numero_secreto <= 100)

class TestTurnoJugadora(unittest.TestCase):

    # Prueba para verificar cuando la jugadora adivina el número secreto
    def test_adivina(self):
        numero_secreto = 42
        lista_jugadora = []
        resultado = turno_jugadora(numero_secreto, lista_jugadora)
        self.assertTrue(resultado)

    # Prueba para verificar cuando la jugadora NO adivina el número secreto
    def test_no_adivina(self):
        numero_secreto = 42
        lista_jugadora = []
        resultado = turno_jugadora(numero_secreto + 1, lista_jugadora)
        self.assertFalse(resultado)

    # Prueba para verificar cuando el número dado es mayor y el número secreto es menor
    # def test_no_adivina_numero_mayor(self):
    #     numero_secreto = 42
    #     lista_jugadora = []
    #     resultado, mensaje = turno_jugadora(numero_secreto + 1, lista_jugadora)
    #     self.assertFalse(resultado)
    #     mensaje_esperado = 'El número secreto es menor'
    #     self.assertEqual(mensaje, mensaje_esperado)

    # Prueba para verificar cuando el número dado es menor y el número secreto es mayor
    # def test_no_adivina_numero_menor(self):
    #     numero_secreto = 42
    #     lista_jugadora = []
    #     resultado, mensaje = turno_jugadora(numero_secreto - 1, lista_jugadora)
    #     self.assertFalse(resultado)
    #     mensaje_esperado = 'El número secreto es mayor'
    #     self.assertEqual(mensaje, mensaje_esperado)

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")