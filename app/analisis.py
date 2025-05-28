"""
Módulo de análisis y visualización de datos de los talleres culturales.

Contiene la clase Analisis, responsable de procesar la información
registrada y generar reportes y gráficos con el uso de pandas y matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

class Analisis:
    """
    Clase para el análisis estadístico y visual de los datos de participantes.

    Atributos:
        df (pd.DataFrame): Conjunto de datos de participantes.
    """

    def __init__(self, participantes):
        """
        Inicializa la clase con un DataFrame de participantes.

        Args:
            Participantes (list): Datos estructurados de los participantes.
        """
        # Convertimos a lista de diccionarios para crear el DataFrame
        self.df = pd.DataFrame([p.to_dict() for p in participantes])

    def total_participantes(self):
        """
        Retorna el total de participantes registrados en el sistema.
        """
        return len(self.df)

    def participantes_incompletos(self):
        """
        Identifica y retorna los participantes con datos nulos o incompletos.
        """
        return self.df[self.df.isnull().any(axis=1)]

    def promedio_pagos_por_taller(self):
        """
        Calcula el promedio de valor pagado por cada tipo de taller.
        """
        return self.df.groupby("taller")["valor_pagado"].mean()

    def taller_mas_popular(self):
        """
        Retorna el taller con mayor cantidad de participantes inscritos.
        """
        return self.df["taller"].value_counts().idxmax()

    def participante_top(self):
        """
        Identifica y retorna el participante con el mayor valor pagado.
        """
        top = self.df.sort_values(by="valor_pagado", ascending=False).iloc[0]
        return top["nombre"]

    def graficar_participacion(self):
        """
        Genera un gráfico de barras con el número de participantes por taller.
        """
        conteo = self.df["taller"].value_counts()
        conteo.plot(kind="bar", title="Participantes por Taller")
        plt.xlabel("Taller")
        plt.ylabel("Número de Participantes")
        plt.tight_layout()
        plt.show()

    def graficar_edades(self):
        """
        Genera un histograma de edades de los participantes.
        """
        self.df["edad"].plot(kind="hist", bins=10, title="Distribución de Edades")
        plt.xlabel("Edad")
        plt.tight_layout()
        plt.show()

    def graficar_pie_talleres(self):
        """
        Genera un gráfico circular que representa la distribución por taller.
        """
        self.df["taller"].value_counts().plot(kind="pie", autopct="%1.1f%%", title="Distribución por Taller")
        plt.ylabel("")
        plt.tight_layout()
        plt.show()
