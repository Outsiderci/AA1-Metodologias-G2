import re

class Usuario:
    base_de_datos = []

    @classmethod
    def registrar(cls, nombre, email, clave):
        if not nombre or not email or not clave:
            return "Error: Datos vacíos"

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Error: Email inválido"

        for user in cls.base_de_datos:
            if user['email'] == email:
                return "Error: Usuario ya registrado"

        if len(clave) < 8:
            return "Error: Contraseña insegura"

        cls.base_de_datos.append({"nombre": nombre, "email": email})
        return "Usuario registrado exitosamente"

    @classmethod
    def resetear_base_de_datos(cls):
        cls.base_de_datos = []