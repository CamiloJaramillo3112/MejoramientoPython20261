from data.registros import usuarios


def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    correo = input("Ingrese su correo: ")
    password = input("Ingrese su contraseña: ")

    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("Ese correo ya está registrado.")
            return

    nuevo_usuario = {
        "correo": correo,
        "password": password
    }

    usuarios.append(nuevo_usuario)
    print("Usuario registrado exitosamente.")


def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    intentos = 4

    while intentos > 0:
        correo = input("Correo: ")
        password = input("Contraseña: ")

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                print("Login exitoso")
                return True

        intentos -= 1

        if intentos > 0:
            print(f"Credenciales incorrectas. Intentos restantes: {intentos}")
        else:
            print("Cuenta bloqueada temporalmente")

    return False