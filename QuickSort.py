import time
import random
import sys

# 1. Implementación de QuickSort
def quicksort(arr: list) -> list:
    """Implementación de QuickSort con partición de Hoare."""
    arr = arr.copy()
    _quicksort_helper(arr, 0, len(arr)-1)
    return arr

def _quicksort_helper(arr: list, low: int, high: int) -> None:
    """Función auxiliar recursiva para QuickSort."""
    if low < high:
        pivot_idx = _partition(arr, low, high)
        _quicksort_helper(arr, low, pivot_idx)
        _quicksort_helper(arr, pivot_idx+1, high)

def _partition(arr: list, low: int, high: int) -> int:
    """Función de partición para QuickSort."""
    pivot = arr[(low + high) // 2]  # Pivote medio
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

# 2. Medición de Rendimiento
def measure_performance(data: list) -> tuple:
    """Mide tiempo y memoria de QuickSort."""
    start_mem = sys.getsizeof(data)
    start_time = time.time()
    sorted_data = quicksort(data)
    end_time = time.time()
    end_mem = sys.getsizeof(sorted_data)

    return (end_time - start_time, max(start_mem, end_mem))

def generate_test_data(size: int, data_type: str = 'random') -> list:
    """Genera datos de prueba consistentes."""
    random.seed(42)
    if data_type == 'random':
        return [random.randint(0, 100000) for _ in range(size)]
    elif data_type == 'sorted':
        return [i for i in range(size)]
    elif data_type == 'reverse':
        return [i for i in range(size, 0, -1)]
    else:
        raise ValueError("Use 'random', 'sorted' o 'reverse'")

# 3. Pruebas de Rendimiento
def run_performance_tests():
    sizes = [100, 500, 1000, 5000, 10000]
    data_types = ['random', 'sorted', 'reverse']
    results = {dtype: {'sizes': [], 'times': [], 'memory': []} for dtype in data_types}

    print("QuickSort Performance:")
    print("Tipo\t| Tamaño\t| Tiempo (s)\t| Memoria (bytes)")
    print("-"*50)

    for dtype in data_types:
        for size in sizes:
            try:
                data = generate_test_data(size, dtype)
                time_taken, mem_used = measure_performance(data)

                results[dtype]['sizes'].append(size)
                results[dtype]['times'].append(time_taken)
                results[dtype]['memory'].append(mem_used)

                print(f"{dtype:<7}\t| {size:<7}\t| {time_taken:.6f}\t| {mem_used}")
            except Exception as e:
                print(f"Error con tamaño {size}: {str(e)}")
                continue
    
    return results

# 6. Explicación del Análisis de Complejidad
def print_complexity_explanation():
    print("\nAnálisis de Complejidad de QuickSort:")
    print("- Caso promedio: O(n log n)")
    print("- Mejor caso: O(n log n) (con partición balanceada)")
    print("- Peor caso: O(n²) (cuando el pivote es siempre el menor/mayor elemento)")

# Ejecución principal
if __name__ == "__main__":
    results = run_performance_tests()
    print_complexity_explanation()
