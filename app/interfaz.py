from app.logica import GestorParticipantes, Participante
from app.analisis import Analisis

import tkinter as tk
from tkinter import messagebox
# https://www.youtube.com/watch?v=sQRrtdbA6jc
from tkinter import ttk # https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=63&codigo=63&inicio=60

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

            self.gestor.registrar_participante(participante)
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
        ventana = tk.Toplevel(self.master)
        ventana.title("Modificar Participante")
        ventana.geometry("400x350")

        tk.Label(ventana, text="Nombre del participante a modificar:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        nombre_buscar = tk.Entry(ventana)
        nombre_buscar.grid(row=0, column=1)

        # Nuevos datos
        campos = {
            "Edad": tk.IntVar(),
            "Taller": tk.StringVar(value="Pintura"),
            "Mes": tk.StringVar(value="Enero"),
            "Clases asistidas": tk.IntVar()
        }

        tk.Label(ventana, text="Edad nueva:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        tk.Spinbox(ventana, from_=5, to=100, textvariable=campos["Edad"]).grid(row=1, column=1)

        tk.Label(ventana, text="Nuevo taller:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        opciones = ["Pintura", "Teatro", "Música", "Danza"]
        tk.OptionMenu(ventana, campos["Taller"], *opciones).grid(row=2, column=1)

        tk.Label(ventana, text="Nuevo mes:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        tk.OptionMenu(ventana, campos["Mes"], *meses).grid(row=3, column=1)

        tk.Label(ventana, text="Nuevas clases:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        tk.Spinbox(ventana, from_=1, to=31, textvariable=campos["Clases asistidas"]).grid(row=4, column=1)

        def modificar():
            nombre = nombre_buscar.get().strip()
            if not nombre:
                messagebox.showerror("Error", "Debe ingresar el nombre.")
                return
            self.gestor.modificar_participante(
                nombre,
                edad=campos["Edad"].get(),
                taller=campos["Taller"].get(),
                mes=campos["Mes"].get(),
                clases_asistidas=campos["Clases asistidas"].get()
            )
            messagebox.showinfo("Éxito", "Participante modificado.")
            ventana.destroy()

        tk.Button(ventana, text="Modificar", command=modificar).grid(row=5, column=0, columnspan=2, pady=20)


    def abrir_formulario_eliminar(self):
        """
        Abre una ventana para buscar y eliminar un participante.
        """
        ventana = tk.Toplevel(self.master)
        ventana.title("Eliminar Participante")
        ventana.geometry("350x150")

        tk.Label(ventana, text="Nombre del participante a eliminar:").pack(pady=10)
        entrada_nombre = tk.Entry(ventana)
        entrada_nombre.pack()

        def eliminar():
            nombre = entrada_nombre.get().strip()
            if not nombre:
                messagebox.showerror("Error", "Debe ingresar un nombre.")
                return
            self.gestor.eliminar_participante(nombre)
            messagebox.showinfo("Éxito", f"Participante '{nombre}' eliminado.")
            ventana.destroy()

        tk.Button(ventana, text="Eliminar", command=eliminar).pack(pady=10)

    def mostrar_registros(self):
        """
        Abre una ventana con una tabla que muestra todos los participantes registrados.
        """
        ventana = tk.Toplevel(self.master)
        ventana.title("Listado de Participantes")
        ventana.geometry("700x400")

        # Crear Treeview
        columnas = ("Nombre", "Edad", "Taller", "Mes", "Clases", "Pago")
        tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
        
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=100, anchor="center")

        tabla.pack(expand=True, fill="both", padx=10, pady=10)

        # Insertar datos
        for p in self.gestor.participantes:
            tabla.insert("", "end", values=(
                p.nombre, p.edad, p.taller, p.mes, p.clases_asistidas, p.calcular_pago()
            ))


    def abrir_menu_reporte(self):
        """
        Abre un submenú con opciones de análisis estadístico y visualización:
        - Total de participantes
        - Participante con mayor pago
        - Taller más popular
        - Gráficos: barras, pie, histograma
        """
    
        ventana = tk.Toplevel(self.master)
        ventana.title("Reportes y Análisis")
        ventana.geometry("400x300")

        analisis = Analisis(self.gestor.obtener_todos())

        def mostrar_total():
            total = analisis.total_participantes()
            messagebox.showinfo("Total participantes", f"Total: {total}")

        def mostrar_top():
            top = analisis.participante_top()
            messagebox.showinfo("Participante Top", f"Mayor pago: {top}")

        def mostrar_popular():
            popular = analisis.taller_mas_popular()
            messagebox.showinfo("Taller más popular", f"Taller: {popular}")

        def graficar_1():
            analisis.graficar_participacion()

        def graficar_2():
            analisis.graficar_edades()

        def graficar_3():
            analisis.graficar_pie_talleres()

        tk.Button(ventana, text="Total participantes", command=mostrar_total).pack(pady=5)
        tk.Button(ventana, text="Participante con mayor pago", command=mostrar_top).pack(pady=5)
        tk.Button(ventana, text="Taller más popular", command=mostrar_popular).pack(pady=5)
        tk.Button(ventana, text="Gráfico de participación", command=graficar_1).pack(pady=5)
        tk.Button(ventana, text="Gráfico de edades", command=graficar_2).pack(pady=5)
        tk.Button(ventana, text="Gráfico de distribución por taller", command=graficar_3).pack(pady=5)


# Ejecución del programa
if __name__ == "__main__":
    root = tk.Tk() # https://www.geeksforgeeks.org/python-gui-tkinter/
    app = VentanaPrincipal(root)
    root.mainloop()
