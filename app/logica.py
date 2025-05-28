import pandas as pd

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
        pass  

    def calcular_pago(self):
        """
        Calcula el valor total a pagar según el número de clases asistidas
        y el taller inscrito. Retorna un entero con el valor total.
        """
        pass

    def to_dict(self):
        """
        Devuelve un diccionario con los atributos del participante.
        Útil para integrarse con pandas o para exportación de datos.
        """
        pass

    def actualizar_datos(self, **kwargs): # https://python-intermedio.readthedocs.io/es/latest/args_and_kwargs.html
        """
        Permite actualizar uno o varios atributos del participante.
        Por ejemplo: edad, mes o número de clases. También recalcula el valor pagado.
        """
        pass