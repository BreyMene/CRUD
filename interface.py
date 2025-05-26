import tkinter as tk
from tkinter import messagebox, simpledialog
from crud import crear_producto, obtener_productos, actualizar_producto, eliminar_producto

def iniciar_interface():
    root = tk.Tk()
    root.title("Gestión de Productos")
    root.geometry("400x450")

    def crear():
        win = tk.Toplevel(root)
        win.title("Crear Producto")
        win.geometry("350x300")

        # Campos
        tk.Label(win, text="Nombre:").pack()
        entry_nombre = tk.Entry(win)
        entry_nombre.pack()

        tk.Label(win, text="Descripción:").pack()
        entry_descripcion = tk.Entry(win)
        entry_descripcion.pack()

        tk.Label(win, text="Precio:").pack()
        entry_precio = tk.Entry(win)
        entry_precio.pack()

        tk.Label(win, text="Cantidad:").pack()
        entry_cantidad = tk.Entry(win)
        entry_cantidad.pack()

        def guardar():
            nombre = entry_nombre.get().strip()
            descripcion = entry_descripcion.get().strip()
            precio_str = entry_precio.get().strip()
            cantidad_str = entry_cantidad.get().strip()

            # Validaciones
            if not nombre or not descripcion or not precio_str or not cantidad_str:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return

            try:
                precio = float(precio_str)
                cantidad = int(cantidad_str)
            except ValueError:
                messagebox.showerror("Error", "Precio debe ser un número decimal y cantidad un número entero.")
                return

            crear_producto(nombre, descripcion, precio, cantidad)
            messagebox.showinfo("Éxito", "Producto creado correctamente.")
            win.destroy()

        tk.Button(win, text="Guardar", command=guardar).pack(pady=10)

    def ver():
        productos = obtener_productos()

        if not productos:
            messagebox.showinfo("Productos", "No hay productos registrados.")
            return

        ventana = tk.Toplevel()
        ventana.title("Lista de Productos")
        ventana.geometry("600x400")

        frame = tk.Frame(ventana)
        frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        texto = tk.Text(frame, wrap=tk.NONE, yscrollcommand=scrollbar.set)
        texto.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=texto.yview)

        encabezado = f"{'ID':<5} | {'Nombre':<15} | {'Descripción':<20} | {'Precio':<10} | {'Cantidad':<8}\n"
        texto.insert(tk.END, encabezado)
        texto.insert(tk.END, "-" * 70 + "\n")

        for p in productos:
            fila = f"{p[0]:<5} | {p[1]:<15} | {p[2]:<20} | ${p[3]:<10.2f} | {p[4]:<8}\n"
            texto.insert(tk.END, fila)

        texto.config(state=tk.DISABLED)


    def actualizar():
        try:
            id_producto = int(simpledialog.askstring("Actualizar Producto", "ID del producto a actualizar:"))
            productos = obtener_productos()
            producto = next((p for p in productos if p[0] == id_producto), None)

            if not producto:
                messagebox.showerror("Error", f"No se encontró ningún producto con ID {id_producto}.")
                return

            # Crear ventana de actualización
            ventana = tk.Toplevel()
            ventana.title("Actualizar Producto")
            ventana.geometry("350x300")

            tk.Label(ventana, text="Nombre:").pack()
            entry_nombre = tk.Entry(ventana)
            entry_nombre.insert(0, producto[1])
            entry_nombre.pack()

            tk.Label(ventana, text="Descripción:").pack()
            entry_descripcion = tk.Entry(ventana)
            entry_descripcion.insert(0, producto[2])
            entry_descripcion.pack()

            tk.Label(ventana, text="Precio:").pack()
            entry_precio = tk.Entry(ventana)
            entry_precio.insert(0, str(producto[3]))
            entry_precio.pack()

            tk.Label(ventana, text="Cantidad:").pack()
            entry_cantidad = tk.Entry(ventana)
            entry_cantidad.insert(0, str(producto[4]))
            entry_cantidad.pack()

            def guardar_actualizacion():
                try:
                    nombre = entry_nombre.get() or producto[1]
                    descripcion = entry_descripcion.get() or producto[2]
                    precio = float(entry_precio.get()) if entry_precio.get() else producto[3]
                    cantidad = int(entry_cantidad.get()) if entry_cantidad.get() else producto[4]

                    actualizar_producto(id_producto, nombre, descripcion, precio, cantidad)
                    messagebox.showinfo("Éxito", "Producto actualizado.")
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Datos inválidos: {e}")

            tk.Button(ventana, text="Guardar cambios", command=guardar_actualizacion).pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"ID inválido: {e}")
            
    def eliminar():
        try:
            id_producto = simpledialog.askstring("Eliminar Producto", "ID del producto a eliminar:")
            if not id_producto or not id_producto.isdigit():
                messagebox.showerror("Error", "Debe ingresar un ID numérico válido.")
                return

            id_producto = int(id_producto)
            productos = obtener_productos()
            if not any(p[0] == id_producto for p in productos):
                messagebox.showwarning("No encontrado", f"No se encontró ningún producto con ID {id_producto}.")
                return

            eliminar_producto(id_producto)
            messagebox.showinfo("Éxito", f"Producto con ID {id_producto} eliminado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar producto: {e}")


    # Botones principales
    tk.Button(root, text="Crear producto", width=30, command=crear).pack(pady=10)
    tk.Button(root, text="Ver productos", width=30, command=ver).pack(pady=10)
    tk.Button(root, text="Actualizar producto", width=30, command=actualizar).pack(pady=10)
    tk.Button(root, text="Eliminar producto", width=30, command=eliminar).pack(pady=10)
    tk.Button(root, text="Salir", width=30, command=root.destroy).pack(pady=10)

    root.mainloop()
