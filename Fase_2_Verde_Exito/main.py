from usuario import Usuario

def main():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE USUARIOS ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar Sesión (Login)")
        print("3. Salir")
        
        opcion = input("Seleccione opción: ")
        
        if opcion == '1':
            print("\n[REGISTRO]")
            nombre = input("Nombre: ")
            email = input("Email: ")
            clave = input("Contraseña: ")
            print(">>", Usuario.registrar(nombre, email, clave))
            
        elif opcion == '2':
            print("\n[LOGIN]")
            email = input("Email: ")
            clave = input("Contraseña: ")
            print(">>", Usuario.iniciar_sesion(email, clave))
            
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()