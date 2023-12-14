# Clase Cliente
class Cliente:
    """
    Clase que representa a un cliente.

    Atributos:
    - nombre (str): El nombre del cliente.
    - edad (int): La edad del cliente.
    - direccion (str): La dirección del cliente.
    - email (str): El correo electrónico del cliente.
    """

    def __init__(self, nombre, edad, direccion, email):
        """
        Inicializa una instancia de la clase Cliente.

        Parámetros:
        - nombre (str): El nombre del cliente.
        - edad (int): La edad del cliente.
        - direccion (str): La dirección del cliente.
        - email (str): El correo electrónico del cliente.
        """
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.email = email

    def comprar(self, producto):
        """
        Realiza la compra de un producto.

        Parámetros:
        - producto (str): El nombre del producto a comprar.
        """
        # Lógica para realizar la compra del producto
        print(f"{self.nombre} ha comprado {producto}")

    def mostrar_informacion(self):
        """
        Muestra la información del cliente.
        """
        # Mostrar información del cliente
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Dirección: {self.direccion}")
        print(f"Email: {self.email}")

    def __str__(self):
        """
        Devuelve el nombre del cliente como representación en cadena.
        """
        return self.nombre


# Crear instancia de Cliente
cliente1 = Cliente("Juan", 25, "Calle Principal 123", "juan@example.com")

# Realizar una compra
cliente1.comprar("Camiseta")

# Mostrar información del cliente
cliente1.mostrar_informacion()
