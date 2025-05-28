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
        from app.logica import GestorParticipantes, Participante
        self.gestor = GestorParticipantes()

        self.master = master
        self.master.title("Sistema de Talleres Culturales")
        self.master.geometry("600x400")
        
        self.configurar_grid()
        self.crear_widgets()

    def configurar_grid(self):
        """
        Configura la estructura de la cuadrícula principal para colocar los botones.
        Se define un layout de 3 filas y 2 columnas con expansión proporcional.
        """
        for i in range(3):
            self.master.rowconfigure(i, weight=1)
        for j in range(2):
            self.master.columnconfigure(j, weight=1)

    def crear_widgets(self):
        """
        Crea y posiciona los botones principales que permiten acceder a las funcionalidades:
        registrar, modificar, eliminar, ver registros y generar reportes.
        """
        boton_registrar = tk.Button(self.master, text="Registrar Participante", command=self.abrir_formulario_registro)
        boton_registrar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        boton_modificar = tk.Button(self.master, text="Modificar Participante", command=self.abrir_formulario_modificar)
        boton_modificar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        boton_eliminar = tk.Button(self.master, text="Eliminar Participante", command=self.abrir_formulario_eliminar)
        boton_eliminar.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        boton_ver_registros = tk.Button(self.master, text="Ver Registros", command=self.mostrar_registros)
        boton_ver_registros.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        boton_reportes = tk.Button(self.master, text="Generar Reporte", command=self.abrir_menu_reporte)
        boton_reportes.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


    def abrir_formulario_registro(self):
        """
        Abre una nueva ventana para registrar un nuevo participante.
        """
        ventana = tk.Toplevel(self.master)
        ventana.title("Registrar Participante")
        ventana.geometry("400x300")
        
        # Variables de control
        self.nombre_var = tk.StringVar()
        self.edad_var = tk.IntVar(value=10)
        self.taller_var = tk.StringVar(value="Pintura")
        self.mes_var = tk.StringVar(value="Enero")
        self.clases_var = tk.IntVar(value=1)


        # Labels y Entradas
        
        # Nombre
        tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        tk.Entry(ventana, textvariable=self.nombre_var).grid(row=0, column=1)

        # Edad
        tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        tk.Spinbox(ventana, from_=5, to=100, textvariable=self.edad_var).grid(row=1, column=1)

        # Taller
        tk.Label(ventana, text="Taller:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        opciones_taller = ["Pintura", "Teatro", "Música", "Danza"]
        tk.OptionMenu(ventana, self.taller_var, *opciones_taller).grid(row=2, column=1)

        # Mes
        tk.Label(ventana, text="Mes:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        tk.OptionMenu(ventana, self.mes_var, *meses).grid(row=3, column=1)

        # Clases asistidas
        tk.Label(ventana, text="Número de clases:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        tk.Spinbox(ventana, from_=1, to=31, textvariable=self.clases_var).grid(row=4, column=1)

        # Boton para registrar
        tk.Button(ventana, text="Registrar", command=self.registrar_participante).grid(row=5, column=0, columnspan=2, pady=20)

   def registrar_participante(self):
        """
        Valida los datos ingresados, crea un participante y lo registra usando el gestor.
        Muestra mensajes de éxito o error al usuario.
        """
        nombre = self.nombre_var.get().strip()
        edad = self.edad_var.get()
        taller = self.taller_var.get()
        mes = self.mes_var.get()
        clases = self.clases_var.get()

        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            participante = Participante(
                nombre=nombre,
                edad=int(edad),
                taller=taller,
                mes=mes,
                clases_asistidas=int(clases)
            )

            self.gestor.agregar_participante(participante)
            messagebox.showinfo("Éxito", f"Participante {nombre} registrado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al registrar: {str(e)}")


        
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
