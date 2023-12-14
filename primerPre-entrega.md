from google.colab import drive
import json
drive.mount('/content/drive/', force_remount=True)

route = "/content/drive/MyDrive/Colab Notebooks/colab_files"
jsonFile = "/users.json"

def getJson(fileToOpen):
    try:
        with open(route + fileToOpen, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except Exception as e:
        print('Error in getJson:')
        print(e)
        return []

def saveJson(fileToOpen, newJson):
    try:
        with open(route + fileToOpen, 'w') as file:
            json.dump(newJson, file, indent=4)
            # Eliminar las contraseñas antes de imprimir
            json_to_print = [{'userName': user.get('userName')} for user in newJson]
            print('Archivo Salvado con la siguiente información: ', json_to_print)
            return True
    except Exception as e:
        print('Error in saveJson:')
        print(e)
        return False

def login():
    try:
        users = getJson(jsonFile)
        print('--- Iniciar Sesión ---')
        name = input('¿Cuál es tu nombre? ')
        while len(name) == 0:
            print('El nombre es requerido.')
            name = input('¿Cuál es tu nombre? ')
        password = input('¿Cuál es tu contraseña? ')
        while len(password) == 0:
            print('La contraseña es requerida.')
            password = input('¿Cuál es tu contraseña? ')
        user = next((u for u in users if u.get('userName') == name and u.get('password') == password), None)
        if user:
            print('¡Bienvenido,', name + '!')
        else:
            print('Nombre de usuario o contraseña incorrectos. Por favor, intenta nuevamente.')
    except Exception as e:
        print('Error in login:')
        print(e)

def getAllUsers():
    try:
        users = getJson(jsonFile)
        print('--- Lista de Usuarios ---')
        for user in users:
            print('Nombre de usuario:', user.get('userName'))
        print('--- Fin de la lista ---')
    except Exception as e:
        print('Hubo un error al consultar los usuarios.')
        print(e)

def register():
    try:
        print('--- Registro de Usuario ---')
        name = input('¿Cuál es tu nombre? ')
        while len(name) == 0:
            print('El nombre es requerido.')
            name = input('¿Cuál es tu nombre? ')
        password = input('¿Cuál es tu contraseña? ')
        while len(password) == 0:
            print('La contraseña es requerida.')
            password = input('¿Cuál es tu contraseña? ')
        newUser = {'userName': name, 'password': password}
        users = getJson(jsonFile)
        users.append(newUser)
        if saveJson(jsonFile, users):
            print(f'¡El usuario {name} se ha registrado exitosamente!')
        else:
            print('Hubo un error registrando al usuario.')
    except Exception as e:
        print('Error in register:')
        print(e)

def main():
    try:
        print('--- Bienvenido al Sistema de Gestión de Usuarios ---')
        while True:
            choice = input('¿Qué quieres hacer? \ningresar (l) | registrarse (r) | consultar usuarios (g) | salir (q) ')
            if choice.lower() in ['l', 'ingresar', 'ingresar (l)']:
                login()
            elif choice.lower() in ['r', 'registrarse', 'registrarse (r)']:
                register()
            elif choice.lower() in ['g', 'consultar usuarios', 'consultar', 'consultar usuarios (g)']:
                getAllUsers()
            elif choice.lower() in ['q', 'salir', 'salir (q)']:
                print('¡Hasta luego!')
                break
            else:
                print('Opción no válida. Por favor, elige una opción correcta.')

    except Exception as e:
        print('Error in main:')
        print(e)

# Llamada a la función principal para iniciar el programa

main()
