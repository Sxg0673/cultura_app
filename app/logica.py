import csv
import os

class Participante:
    """
    Representa a un participante de un taller cultural.

    Atributos:
        nombre (str): Nombre del participante.
        edad (int): Edad del participante.
        taller (str): Nombre del taller inscrito.
        mes (str): Mes de participación.
        clases_asistidas (int): Número de clases asistidas.
        valor_pagado (int): Valor total calculado con base en el taller y clases.
    """

    # Valores por clase según taller
    tarifas_por_taller = {
        "Pintura": 6000,
        "Teatro": 8000,
        "Música": 10000,
        "Danza": 7000
    }

    def __init__(self, nombre, edad, taller, mes, clases_asistidas):
        """
        Inicializa un nuevo participante con sus datos básicos.
        Calcula automáticamente el valor pagado con base en taller y clases.
        """
        self.nombre = nombre
        self.edad = edad
        self.taller = taller
        self.mes = mes
        self.clases_asistidas = clases_asistidas
        self.valor_pagado = self.calcular_pago()  

    def calcular_pago(self):
        """
        Calcula el valor total a pagar según el número de clases asistidas
        y el taller inscrito. Retorna un entero con el valor total.
        """
        # Obtengo el taller y me aseguro que se encuentre en los talleres establecidos y cambia el valor 0 por el del taller
        tarifa = self.tarifas_por_taller.get(self.taller, 0) 
        return tarifa * self.clases_asistidas

    def to_dict(self):
        """
        Devuelve un diccionario con los atributos del participante.
        Útil para integrarse con pandas o para exportación de datos.
        """
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "taller": self.taller,
            "mes": self.mes,
            "clases_asistidas": self.clases_asistidas,
            "valor_pagado": self.valor_pagado
        }

    # De esta manera nos aseguramos de actualizar los datos que se quieran actualizar y no todos
    def actualizar_datos(self, **kwargs): # https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
        """
        Permite actualizar uno o varios atributos del participante.
        Por ejemplo: edad, mes o número de clases. También recalcula el valor pagado.
        """
        for clave, valor in kwargs.items():
            # Esto verifica si existe
            if hasattr(self, clave): # https://micro.recursospython.com/recursos/la-funcion-hasattr.html
                # Esto lo actualiza
                setattr(self, clave, valor) # https://www.w3schools.com/python/ref_func_setattr.asp
                
        # Recalcula el valor si se cambia el taller o las clases
        if "taller" in kwargs or "clases_asistidas" in kwargs:
            self.valor_pagado = self.calcular_pago()
    
    
class GestorParticipantes:
    """
    Clase que se encarga de gestionar el conjunto de participantes registrados.
    Permite registrar, modificar, eliminar y consultar participantes.
    """

    def __init__(self):
        """
        Inicializa la lista o estructura de datos para almacenar participantes.
        """
        pass

    def registrar_participante(self, participante):
        """
        Agrega un nuevo participante al sistema.

        Args:
            participante (Participante): Objeto participante previamente creado.
        """
        pass

    def modificar_participante(self, nombre, **kwargs):
        """
        Busca un participante por nombre y actualiza sus datos.

        Args:
            nombre (str): Nombre del participante a buscar.
            kwargs: Campos a modificar (edad, taller, etc.)
        """
        pass

    def eliminar_participante(self, nombre):
        """
        Elimina un participante del sistema según su nombre.

        Args:
            nombre (str): Nombre del participante a eliminar.
        """
        pass

    def obtener_todos(self):
        """
        Devuelve la lista completa de participantes registrados.
        """
        pass

    def guardar_en_archivo(self, ruta):
        """
        Guarda todos los participantes en un archivo CSV.

        Args:
            ruta (str): Ruta donde se almacenará el archivo.
        """
        pass

    def cargar_desde_archivo(self, ruta):
        """
        Carga los participantes desde un archivo CSV.

        Args:
            ruta (str): Ruta del archivo con los datos.
        """
        pass