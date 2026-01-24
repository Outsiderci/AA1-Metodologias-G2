from usuario import Usuario

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE USUARIOS ---")
    print("1. Registrar nuevo usuario")
    print("2. Salir")
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            print("\n--- REGISTRO ---")
            nombre = input("Ingrese nombre: ")
            email = input("Ingrese email: ")
            clave = input("Ingrese contraseña: ")
            
            resultado = Usuario.registrar(nombre, email, clave)
            print(f">> RESULTADO: {resultado}")
            
        elif opcion == '2':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()