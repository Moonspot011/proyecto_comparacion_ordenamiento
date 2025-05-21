import time
import random
import sys
from typing import List, Tuple

def quicksort(arr: List[int]) -> List[int]:
    """
    Implementación del algoritmo QuickSort con partición de Hoare.
    
    Args:
        arr: Lista de elementos a ordenar.
        
    Returns:
        Lista ordenada.
    """
    # Caso base: listas vacías o con un elemento ya están ordenadas
    if len(arr) <= 1:
        return arr
    
    # Hacemos una copia para no modificar la lista original
    arr = arr.copy()
    
    # Llamamos a la función auxiliar que implementa el ordenamiento
    _quicksort_helper(arr, 0, len(arr) - 1)
    return arr

def _quicksort_helper(arr: List[int], low: int, high: int) -> None:
    """
    Función auxiliar recursiva para QuickSort.
    
    Args:
        arr: Lista a ordenar.
        low: Índice inferior del segmento a ordenar.
        high: Índice superior del segmento a ordenar.
    """
    if low < high:
        # Obtenemos el índice del pivote después de la partición
        pivot_idx = _partition(arr, low, high)
        
        # Ordenamos recursivamente los elementos antes y después del pivote
        _quicksort_helper(arr, low, pivot_idx)
        _quicksort_helper(arr, pivot_idx + 1, high)

def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Función de partición para QuickSort (versión de Hoare).
    
    Args:
        arr: Lista a particionar.
        low: Índice inferior del segmento.
        high: Índice superior del segmento.
        
    Returns:
        Índice del pivote después de la partición.
    """
    # Elegimos el pivote como el elemento en la posición media
    pivot = arr[(low + high) // 2]
    
    i = low - 1
    j = high + 1
    
    while True:
        # Avanzamos i hasta encontrar un elemento >= pivote
        i += 1
        while arr[i] < pivot:
            i += 1
            
        # Retrocedemos j hasta encontrar un elemento <= pivote
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # Si los índices se cruzan, retornamos j
        if i >= j:
            return j
            
        # Intercambiamos los elementos en i y j
        arr[i], arr[j] = arr[j], arr[i]

def measure_performance(data: List[int]) -> Tuple[float, int]:
    """
    Mide el tiempo de ejecución y uso de memoria de QuickSort.
    
    Args:
        data: Lista de datos a ordenar.
        
    Returns:
        Tupla con (tiempo de ejecución en segundos, uso de memoria en bytes).
    """
    # Medimos memoria antes de la ejecución
    start_mem = sys.getsizeof(data)
    
    # Medimos tiempo de ejecución
    start_time = time.time()
    sorted_data = quicksort(data)
    end_time = time.time()
    
    # Medimos memoria después de la ejecución
    end_mem = sys.getsizeof(sorted_data)
    
    execution_time = end_time - start_time
    memory_usage = max(start_mem, end_mem)  # Tomamos el máximo como estimación
    
    return (execution_time, memory_usage)

def generate_test_data(size: int, data_type: str = 'random') -> List[int]:
    """
    Genera datos de prueba para el algoritmo.
    
    Args:
        size: Tamaño de la lista a generar.
        data_type: Tipo de datos ('random', 'sorted', 'reverse').
        
    Returns:
        Lista generada según el tipo especificado.
    """
    if data_type == 'random':
        return [random.randint(0, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return [i for i in range(size)]
    elif data_type == 'reverse':
        return [i for i in range(size, 0, -1)]
    else:
        raise ValueError("Tipo de dato no válido. Use 'random', 'sorted' o 'reverse'.")

# Ejemplo de uso
if __name__ == "__main__":
    # Generar datos de prueba
    test_data = generate_test_data(100, 'random')
    print(f"Datos originales (primeros 10 elementos): {test_data[:100]}")
    
    # Ordenar y medir rendimiento
    execution_time, memory_usage = measure_performance(test_data)
    sorted_data = quicksort(test_data)
    
    print(f"Datos ordenados (primeros 10 elementos): {sorted_data[:100]}")
    print(f"Tiempo de ejecución: {execution_time:.6f} segundos")
    print(f"Uso de memoria estimado: {memory_usage} bytes")
    
    # Verificar que el ordenamiento es correcto
    assert sorted_data == sorted(test_data), "El ordenamiento no es correcto!"
    print("El ordenamiento es correcto.")