import unittest
from usuario import Usuario

class TestGestionUsuarios(unittest.TestCase):
    
    def setUp(self):
        Usuario.resetear_base_de_datos()

    def test_1_registro_exitoso(self):
        resultado = Usuario.registrar("Kevin", "admin@espe.edu.ec", "Sistemas2026")
        self.assertEqual(resultado, "Usuario registrado exitosamente")

    def test_2_clave_corta(self):
        resultado = Usuario.registrar("Hacker", "malo@hack.com", "123")
        self.assertEqual(resultado, "Error: Contraseña insegura")

    def test_3_email_invalido(self):
        resultado = Usuario.registrar("Kevin", "kevin-sin-arroba.com", "ClaveFuerte1")
        self.assertEqual(resultado, "Error: Email inválido")

    def test_4_usuario_duplicado(self):
        Usuario.registrar("Kevin", "unico@espe.edu.ec", "ClaveFuerte1")
        resultado = Usuario.registrar("Otro", "unico@espe.edu.ec", "ClaveFuerte1")
        self.assertEqual(resultado, "Error: Usuario ya registrado")

if __name__ == '__main__':
    unittest.main()