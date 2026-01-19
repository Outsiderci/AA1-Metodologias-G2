import unittest
from usuario import Usuario

class TestRegistroUsuario(unittest.TestCase):
    def test_registro_exitoso(self):
        resultado = Usuario.registrar("Kevin", "kevin@espe.edu.ec", "Segura123")
        self.assertEqual(resultado, "Usuario registrado con éxito")

    def test_clave_corta(self):
        resultado = Usuario.registrar("Kevin", "kevin@espe.edu.ec", "123")
        self.assertEqual(resultado, "Error: Contraseña muy corta")

if __name__ == '__main__':
    unittest.main()