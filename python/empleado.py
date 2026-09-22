class Empleado:
    def __init__(self, nombre,cargo):
        self.nombre = nombre
        self.cargo = cargo

class Tarea:
    def __init__(self, nombre, responsable):
        self.nombre=nombre
        self.responsable=responsable 

empleado = Empleado("Juan Diego","Ingeniero de Soporte")
tarea= Tarea("Soporte Nivel 3 con su usuario","Juan Diego")
print(empleado.nombre, "-", tarea.nombre)

empleado = Empleado("Juan Camilo", " Ingeniero ML")
tarea = Tarea("Generar Datasets", "Juan Camilo")
print (empleado.nombre, "-", tarea.nombre)