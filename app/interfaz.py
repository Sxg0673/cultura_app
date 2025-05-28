from logica import GestorParticipantes
from analisis import Analisis

import tkinter as tk
from tkinter import messagebox

class VentanaPrincipal:
    """
    Clase que define la interfaz gráfica principal del sistema de talleres culturales.
    Utiliza Tkinter para construir la ventana, botones y organización visual.
    """

    def __init__(self, master): # https://www.youtube.com/watch?v=epDKamC-V-8
        """
        Inicializa la ventana principal y configura el diseño base con grid.
        
        Args:
            master: ventana raíz de Tkinter.
        """
        self.master = master
        self.master.title("Sistema de Talleres Culturales")
        self.master.geometry("600x400")
        
        self.configurar_grid()
        self.crear_widgets()

    def configurar_grid(self):
        """
        Configura la estructura de la cuadrícula para el posicionamiento con grid().
        """
        pass

    def crear_widgets(self):
        """
        Crea los botones principales de la interfaz y los posiciona en la ventana.
        Cada botón está asociado a una funcionalidad del sistema.
        """
        pass

    def abrir_formulario_registro(self):
        """
        Abre una nueva ventana para registrar un nuevo participante.
        """
        ventana = tk.Toplevel(self.master)
        ventana.title("Registrar Participante")
        ventana.geometry("400x300")

        # Labels y Entradas
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.grid(row=0, column=1)

        tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        entrada_edad = tk.Entry(ventana)
        entrada_edad.grid(row=1, column=1)

        tk.Label(ventana, text="Taller:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        talleres = ["Pintura", "Teatro", "Música", "Danza"]
        variable_taller = tk.StringVar(value=talleres[0])
        menu_taller = tk.OptionMenu(ventana, variable_taller, *talleres)
        menu_taller.grid(row=2, column=1)

        tk.Label(ventana, text="Mes:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        entrada_mes = tk.Entry(ventana)
        entrada_mes.grid(row=3, column=1)

        tk.Label(ventana, text="Número de clases:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        entrada_clases = tk.Entry(ventana)
        entrada_clases.grid(row=4, column=1)
        
        def guardar_participante():
            """
            Toma los datos del formulario, valida que estén completos, los transforma y los guarda.
            """
            nombre = entrada_nombre.get().strip()
            edad = entrada_edad.get().strip()
            taller = variable_taller.get()
            mes = entrada_mes.get().strip()
            clases = entrada_clases.get().strip()

            if not nombre or not edad or not mes or not clases:
                messagebox.showerror("Error", "Por favor complete todos los campos.")
                return

            try:
                edad = int(edad)
                clases = int(clases)
            except ValueError:
                messagebox.showerror("Error", "Edad y número de clases deben ser números.")
                return

            self.gestor.registrar_participante(nombre, edad, taller, mes, clases)
            messagebox.showinfo("Éxito", "Participante registrado correctamente.")
            ventana.destroy()

        # Botón para guardar
        boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_participante)
        boton_guardar.grid(row=5, column=0, columnspan=2, pady=20)

    def abrir_formulario_modificar(self):
        """
        Abre una ventana para buscar y modificar datos de un participante.
        """
        pass

    def abrir_formulario_eliminar(self):
        """
        Abre una ventana para buscar y eliminar un participante.
        """
        pass

    def mostrar_registros(self):
        """
        Muestra todos los registros de participantes en una nueva ventana o tabla.
        """
        pass

    def abrir_menu_reporte(self):
        """
        Abre un submenú con opciones de análisis estadístico y visualización:
        - Total de participantes
        - Participante con mayor pago
        - Taller más popular
        - Gráficos: barras, pie, histograma
        """
        pass

# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk() # https://www.geeksforgeeks.org/python-gui-tkinter/
    app = VentanaPrincipal(root)
    root.mainloop()
