'''
Crea una clase Persona con atributos nombre y edad. Agrega un método
saludar() que imprima "Hola, mi nombre es [nombre] y tengo [edad] años".
Crea un objeto persona1 e invoca el método saludar()
'''
from Persona import Persona
from Empleado import Empleado
from Producto import Producto
from Libro import Libro
from Calculadora import Calculadora

p1 = Persona("Nahuel", 25)
p1.saludar()

'''
Define una clase Empleado que herede de Persona y tenga un atributo
adicional salario. Implementa un método mostrar_salario() que imprima "El
salario es [salario]" el salario deberá salir con el iva incluido.
Crea un Empleado y muestra su saludo y salario.
'''
e1 = Empleado("Nahuel", 24, 2000)
e1.saludar()
e1.imprimir_salario()

'''
Crea una clase Producto con atributos nombre y precio. Implementa un
diccionario para almacenar productos como claves y sus cantidades como
valores.
Agrega productos, actualiza cantidades y muestra la información completa del
inventario.
'''
almacenProductos = {  }
prod1 = Producto("Movil", 799)
prod2 = Producto ("Consola", 499)
almacenProductos[prod1.nombre] = { "cantidad": 32}
almacenProductos[prod2.nombre] = {"cantidad": 10}
almacenProductos["Movil"] = {55}
print(almacenProductos)

'''
Redefine los métodos __eq__ y __hash__ en la clase Libro para que los
objetos se puedan usar como claves de un diccionario que almacene el número
de copias.
Usa el diccionario para registrar libros y consulta el número total de copias de
un título específico.
'''
libreria = {}
libro1 = Libro("Libro 1", "Yo", "2457345")
libro2 = Libro("Libro 2", "Tú", "45737645")
libreria[libro1.__hash__()] = {"Copias": 10}
libreria[libro2.__hash__()] = {"Copias": 15}

print(libreria[libro1.__hash__()])
print(libreria)

'''
5. Dada una lista de nombres, crea un conjunto para eliminar duplicados.
Muestra la lista original y la lista sin duplicados
'''
nombres = ["Nahuel", "Laura", "Luis", "Sara", "Manu", "Nahuel", "Isa"]
print(list(set(nombres)))

'''
6. Crea dos conjuntos registrados y aprobados. Usa intersección para obtener los
alumnos que están en ambas listas y diferencia para los registrados que no
aprobaron.
Muestra ambos resultados.
'''
alumnosRegistrados = ["Nahuel", "Laura", "Luis", "Sara", "Manu", "Nahuel", "Isa"]
alumnosAprobados = ["Nahuel", "Luis", "Manu"]
print(list(set(alumnosRegistrados).intersection(set(alumnosAprobados))))
print((list(set(alumnosRegistrados).difference(set(alumnosAprobados)))))

'''
7. Crea una clase Calculadora con métodos estáticos para sumar, restar,
multiplicar y dividir.
Llama a los métodos directamente desde la clase sin crear un objeto.
'''
print(Calculadora.sumar(Calculadora(2, 5)))
print(Calculadora.restar(Calculadora(2, 5)))
print(Calculadora.multiplicar(Calculadora(2, 5)))
print(Calculadora.dividir(Calculadora(5, 2)))

'''
8. Implementa una clase Agenda con un diccionario para almacenar contactos
(nombre: teléfono). Crea métodos para agregar, eliminar y buscar contactos.
Agrega varios contactos, búscalos y elimínalos.
'''



'''
9. Crea una clase Empleado con atributos nombre y salario, y investiga __lt__
para comparar empleados por salario.
Ordena una lista de empleados por salario
'''

'''
Crea una clase Texto que almacene un texto. Implementa un método que
cuente las palabras únicas usando un conjunto, y otro que devuelva un
diccionario con la frecuencia de cada palabra.
Usa ambos métodos con un párrafo y muestra los resultados.
'''
