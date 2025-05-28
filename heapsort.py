import time
import random
import sys

def heapsort(arr: list) -> list:
    """
    Implementación del algoritmo HeapSort.
    
    Args:
        arr: Lista a ordenar
        
    Returns:
        Lista ordenada
    """
    n = len(arr)
    arr = arr.copy()  # No modificar el original
    
    # Construir max-heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    # Extraer elementos uno por uno
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Intercambiar
        _heapify(arr, i, 0)
    
    return arr

def _heapify(arr: list, n: int, i: int) -> None:
    """
    Función auxiliar para convertir un subárbol en un max-heap.
    
    Args:
        arr: Lista/array a heapificar
        n: Tamaño del heap
        i: Índice del nodo raíz del subárbol
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

def measure_performance(data: list) -> tuple:
    """
    Mide tiempo de ejecución y memoria estimada de HeapSort.
    
    Args:
        data: Lista de datos a ordenar
        
    Returns:
        Tupla con (tiempo_ejecucion, memoria_estimada_en_bytes)
    """
    # Medir memoria antes (estimación simple)
    start_mem = sys.getsizeof(data)
    
    # Medir tiempo
    start_time = time.time()
    sorted_data = heapsort(data.copy())
    end_time = time.time()
    
    # Medir memoria después
    end_mem = sys.getsizeof(sorted_data)
    
    return (end_time - start_time, max(start_mem, end_mem))

def generate_test_data(size: int, data_type: str = 'random') -> list:
    """
    Genera datos de prueba con semilla fija para consistencia.
    
    Args:
        size: Tamaño de la lista a generar
        data_type: Tipo de datos ('random', 'sorted', 'reverse')
        
    Returns:
        Lista generada
    """
    random.seed(42)  # Semilla fija para reproducibilidad
    if data_type == 'random':
        return [random.randint(0, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return [i for i in range(size)]
    elif data_type == 'reverse':
        return [i for i in range(size, 0, -1)]
    else:
        raise ValueError("Tipo de dato no válido. Use 'random', 'sorted' o 'reverse'.")

def print_complexity_analysis(results: dict, sizes: list):
    """
    Muestra análisis de complejidad en forma de tabla por consola.
    
    Args:
        results: Diccionario con los resultados de las pruebas
        sizes: Lista de tamaños usados en las pruebas
    """
    print("\nAnálisis de complejidad:")
    print("Tipo\t| Tamaño\t| T(n)\t| T(n)/nlog(n)")
    print("-"*50)
    
    # Calcular factores de complejidad
    for dtype in results:
        print(f"\n{dtype.upper()}:")
        for i, size in enumerate(sizes):
            if i == 0:
                ratio = 0
            else:
                n = size
                nlogn = n * (n.bit_length() - 1)  # Aproximación de n*log2(n)
                ratio = results[dtype]['times'][i] / nlogn
            
            print(f"{dtype:<7}\t| {size:<7}\t| {results[dtype]['times'][i]:.6f}\t| {ratio:.6f}")

def run_analysis():
    """Ejecuta el análisis completo de HeapSort y muestra los resultados."""
    # Configuración de pruebas
    sizes = [100, 500, 1000, 5000, 10000, 20000, 50000, 100000]
    data_types = ['random', 'sorted', 'reverse']

    # Almacenar resultados
    results = {dtype: {'sizes': [], 'times': [], 'memory': []} for dtype in data_types}

    print("Rendimiento de HeapSort:")
    print("Tipo\t| Tamaño\t| Tiempo (s)\t| Memoria (bytes)")
    print("-"*60)

    for dtype in data_types:
        for size in sizes:
            data = generate_test_data(size, dtype)
            time_taken, mem_used = measure_performance(data)
            
            results[dtype]['sizes'].append(size)
            results[dtype]['times'].append(time_taken)
            results[dtype]['memory'].append(mem_used)
            
            print(f"{dtype:<7}\t| {size:<7}\t| {time_taken:.6f}\t| {mem_used}")

    # Análisis de complejidad por consola
    print_complexity_analysis(results, sizes)

if __name__ == "__main__":
    run_analysis()
