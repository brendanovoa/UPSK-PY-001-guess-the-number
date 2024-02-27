import unittest
from unittest.mock import patch
from main import generar_numero_secreto, turno_jugadora, nuevo_juego

class TestJuego(unittest.TestCase):

    # Prueba para asegurar que el número secreto está entre 1 y 100
    def test_generar_numero_secreto(self):
        numero_secreto = generar_numero_secreto()
        self.assertTrue(1 <= numero_secreto <= 100)

class TestTurnoJugadora(unittest.TestCase):

    # Prueba para verificar cuando la jugadora adivina el número secreto
    @patch('builtins.input', side_effect=['42'])
    def test_adivina(self, mock_input):
        numero_secreto = 42
        lista_jugadora = []
        resultado = turno_jugadora(numero_secreto, lista_jugadora)
        self.assertTrue(resultado)

    # Prueba para verificar cuando la jugadora NO adivina el número secreto
    @patch('builtins.input', side_effect=['43'])
    def test_no_adivina(self, mock_input):
        numero_secreto = 42
        lista_jugadora = []
        resultado = turno_jugadora(numero_secreto, lista_jugadora)
        self.assertFalse(resultado)

class TestNuevoJuego(unittest.TestCase):

    # Prueba para verificar que se vuelve a jugar si la usuaria responde s
    @patch('builtins.input', side_effect=['s'])
    def test_jugar_de_nuevo_si(self, mock_input):
        resultado = nuevo_juego()
        self.assertTrue(resultado)

    # Prueba para verificar que NO se vuelve a jugar si la usuaria responde n
    @patch('builtins.input', side_effect=['n'])
    def test_jugar_de_nuevo_no(self, mock_input):
        resultado = nuevo_juego()
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()

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