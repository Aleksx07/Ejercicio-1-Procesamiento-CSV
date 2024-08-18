import csv  # Importa el módulo csv para trabajar con archivos CSV
from collections import Counter  

# Clase que representa a una persona con sus atributos básicos
class Persona:
    def __init__(self, nombre, apellido, edad, salario, deducciones, genero):
        self.nombre = nombre  
        self.apellido = apellido  
        self.edad = int(edad) 
        self.salario = int(salario)  
        self.deducciones = int(deducciones)  
        self.genero = genero  

# Clase que procesa un archivo CSV y realiza varias operaciones sobre los datos
class ProcesadorCSV:
    def __init__(self, archivo):
        self.personas = self.cargar_datos(archivo)  # Carga los datos del archivo CSV al iniciar la clase

    # Método para cargar los datos del archivo CSV y convertirlos en instancias de la clase Persona
    def cargar_datos(self, archivo):
        personas = []  
        with open(archivo, 'r') as f: 
            lector = csv.reader(f)  
            next(lector) 
            for fila in lector:  
                personas.append(Persona(*fila))  
        return personas  

    # Método para encontrar la persona con mayor edad
    def persona_con_mayor_edad(self):
        return max(self.personas, key=lambda p: p.edad) 

    # Método para encontrar la persona con menor edad
    def persona_con_menor_edad(self):
        return min(self.personas, key=lambda p: p.edad)  

    # Método para contar cuántos hombres y mujeres hay en la lista
    def M_F(self):
        generos = Counter(p.genero for p in self.personas)  
        return generos  

    # Método para calcular el salario promedio de las personas en la lista
    def promedio_salario(self):
        total_salario = sum(p.salario for p in self.personas)  
        return total_salario / len(self.personas) 

    # Método para encontrar la persona con más deducciones
    def persona_con_mas_deducciones(self):
        return max(self.personas, key=lambda p: p.deducciones) 

    # Método para encontrar la persona con el salario más alto
    def persona_con_mayor_salario(self):
        return max(self.personas, key=lambda p: p.salario)  

# Uso del programa
proccess = ProcesadorCSV('archivoCSV.csv')  # Crea una instancia de ProcesadorCSV y carga los datos de 'archivo.csv'
print('Persona con mayor edad:', proccess.persona_con_mayor_edad().nombre) 
print('Persona con menor edad:', proccess.persona_con_menor_edad().nombre)   
print('Conteo de generos:', proccess.M_F()) 
print('Promedio de salario:', proccess.promedio_salario())  
print('Persona con más deducciones:',
      proccess.persona_con_mas_deducciones().nombre) 
print('Persona con mayor salario:', proccess.persona_con_mayor_salario().nombre)  