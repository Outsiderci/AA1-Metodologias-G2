class Usuario:
    @staticmethod
    def registrar(nombre, email, clave):
        if len(clave) < 6:
            return "Error: Contraseña muy corta"
            
        return "Usuario registrado con éxito"