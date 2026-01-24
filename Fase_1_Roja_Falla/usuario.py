class Usuario:
    base_de_datos = []

    @classmethod
    def registrar(cls, nombre, email, clave):
        if not nombre or not email or not clave:
            return "Error: Datos vacíos"
        
        cls.base_de_datos.append({"nombre": nombre, "email": email})
        return "Usuario registrado exitosamente"

    @classmethod
    def resetear_base_de_datos(cls):
        cls.base_de_datos = []