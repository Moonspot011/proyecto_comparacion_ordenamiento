import matplotlib.pyplot as plt
import numpy as np
import time
import random
from tabulate import tabulate

# Función para formatear el tiempo en unidades legibles
def format_tiempo(seconds):
    if seconds < 1e-6:  # Menos de 1 μs
        return f"{seconds * 1e9:.1f} ns"
    elif seconds < 1e-3:  # Menos de 1 ms
        return f"{seconds * 1e6:.1f} μs"
    elif seconds < 1:  # Menos de 1 segundo
        return f"{seconds * 1000:.1f} ms"
    else:
        return f"{seconds:.3f} s"

# Función para generar diferentes tipos de conjuntos de datos
def generar_datos(tamano, tipo='aleatorio'):
    """
    Genera conjuntos de datos de diferentes tipos:
    - 'aleatorio': Datos aleatorios
    - 'ordenado': Datos ordenados de menor a mayor
    - 'inverso': Datos ordenados de mayor a menor
    """
    if tipo == 'aleatorio':
        return [random.randint(1, 10000) for _ in range(tamano)]
    elif tipo == 'ordenado':
        return sorted([random.randint(1, 10000) for _ in range(tamano)])
    elif tipo == 'inverso':
        return sorted([random.randint(1, 10000) for _ in range(tamano)], reverse=True)
    else:
        raise ValueError("Tipo no válido. Usar 'aleatorio', 'ordenado' o 'inverso'")

# Implementación de BubbleSort con conteo de operaciones
def bubble_sort(lista):
    n = len(lista)
    comparaciones = 0
    intercambios = 0
    
    for i in range(n):
        # Bandera para optimización
        hubo_intercambio = False
        
        for j in range(0, n-i-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambios += 1
                hubo_intercambio = True
                
        # Si no hubo intercambios, la lista ya está ordenada
        if not hubo_intercambio:
            break
            
    return comparaciones, intercambios

# Configuración de pruebas
tamanos = [10, 50, 100, 500, 1000]
tipos_datos = ['aleatorio', 'ordenado', 'inverso']
resultados = []

# Realizar pruebas para cada combinación de tamaño y tipo
for tamano in tamanos:
    for tipo in tipos_datos:
        datos = generar_datos(tamano, tipo)
        
        inicio = time.perf_counter()  # Más preciso que time.time()
        comparaciones, intercambios = bubble_sort(datos.copy())
        tiempo = time.perf_counter() - inicio
        
        resultados.append({
            'Tamaño': tamano,
            'Tipo': tipo,
            'Comparaciones': comparaciones,
            'Intercambios': intercambios,
            'Tiempo (s)': tiempo
        })

# Mostrar resultados en tabla
tabla_resultados = []
for res in resultados:
    tabla_resultados.append([
        res['Tamaño'],
        res['Tipo'],
        res['Comparaciones'],
        res['Intercambios'],
        format_tiempo(res['Tiempo (s)'])  # Usamos la función de formato
    ])

headers = ["Tamaño", "Tipo de Datos", "Comparaciones", "Intercambios", "Tiempo"]
print(tabulate(tabla_resultados, headers=headers, tablefmt="grid"))

# Crear gráficos comparativos
fig, axs = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Análisis de BubbleSort con Diferentes Tipos de Datos', fontsize=16)

# Gráfico 1: Tiempo de ejecución por tamaño y tipo
for tipo in tipos_datos:
    datos_tipo = [r for r in resultados if r['Tipo'] == tipo]
    tamanos_tipo = [d['Tamaño'] for d in datos_tipo]
    tiempos_tipo = [d['Tiempo (s)'] for d in datos_tipo]
    
    axs[0, 0].plot(tamanos_tipo, tiempos_tipo, marker='o', label=tipo.capitalize())

axs[0, 0].set_title('Tiempo de Ejecución vs Tamaño de Datos')
axs[0, 0].set_xlabel('Tamaño de los Datos')
axs[0, 0].set_ylabel('Tiempo (segundos)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Gráfico 2: Comparaciones por tamaño y tipo
for tipo in tipos_datos:
    datos_tipo = [r for r in resultados if r['Tipo'] == tipo]
    tamanos_tipo = [d['Tamaño'] for d in datos_tipo]
    comp_tipo = [d['Comparaciones'] for d in datos_tipo]
    
    axs[0, 1].plot(tamanos_tipo, comp_tipo, marker='o', label=tipo.capitalize())

# Añadir línea teórica O(n^2)
n_vals = np.array(tamanos)
axs[0, 1].plot(n_vals, n_vals**2 / 100, 'k--', label='O(n²) teórico')

axs[0, 1].set_title('Número de Comparaciones vs Tamaño de Datos')
axs[0, 1].set_xlabel('Tamaño de los Datos')
axs[0, 1].set_ylabel('Número de Comparaciones')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Gráfico 3: Intercambios por tamaño y tipo
for tipo in tipos_datos:
    datos_tipo = [r for r in resultados if r['Tipo'] == tipo]
    tamanos_tipo = [d['Tamaño'] for d in datos_tipo]
    interc_tipo = [d['Intercambios'] for d in datos_tipo]
    
    axs[1, 0].plot(tamanos_tipo, interc_tipo, marker='o', label=tipo.capitalize())

axs[1, 0].set_title('Número de Intercambios vs Tamaño de Datos')
axs[1, 0].set_xlabel('Tamaño de los Datos')
axs[1, 0].set_ylabel('Número de Intercambios')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Gráfico 4: Comparación de complejidades teóricas
n_vals = np.linspace(1, 1000, 100)
axs[1, 1].plot(n_vals, n_vals**2, 'r-', label="O(n²) - BubbleSort")
axs[1, 1].plot(n_vals, n_vals * np.log2(n_vals), 'g-', label="O(n log n) - MergeSort")
axs[1, 1].plot(n_vals, n_vals, 'b-', label="O(n) - Búsqueda lineal")
axs[1, 1].set_title('Comparación de Complejidades Teóricas')
axs[1, 1].set_xlabel('Tamaño de Entrada (n)')
axs[1, 1].set_ylabel('Operaciones')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

# Gráfico adicional: Tiempo por tipo de datos (promedio)
fig2, ax = plt.subplots(figsize=(10, 6))
tiempos_promedio = {}

for tipo in tipos_datos:
    tiempos = [r['Tiempo (s)'] for r in resultados if r['Tipo'] == tipo]
    tiempos_promedio[tipo] = np.mean(tiempos)

ax.bar(tipos_datos, tiempos_promedio.values(), color=['skyblue', 'lightgreen', 'salmon'])
ax.set_title('Tiempo Promedio de Ejecución por Tipo de Datos')
ax.set_xlabel('Tipo de Datos')
ax.set_ylabel('Tiempo Promedio (s)')
ax.grid(axis='y')

for i, v in enumerate(tiempos_promedio.values()):
    ax.text(i, v + 0.0001, f"{v:.6f}", ha='center')

plt.show()