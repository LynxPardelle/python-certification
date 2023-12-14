# Clase Cliente
class Cliente:
    def __init__(self, nombre, edad, direccion, email):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.email = email

    def comprar(self, producto):
        # Lógica para realizar la compra del producto
        print(f"{self.nombre} ha comprado {producto}")

    def mostrar_informacion(self):
        # Mostrar información del cliente
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")


# Crear instancia de Cliente
cliente1 = Cliente("Juan", 25, "Calle Principal 123", "juan@example.com")

# Realizar una compra
cliente1.comprar("Camiseta")

# Mostrar información del cliente
cliente1.mostrar_informacion()
