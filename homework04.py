"""
goit-algo-hw-04: Алгоритми сортування — Timsort, Merge Sort, Insertion Sort

Цей скрипт:
1. Реалізує три алгоритми сортування.
2. Порівнює їх за часом виконання на різних об'ємах даних.
3. Будує графік для візуального аналізу.
4. Пояснює, чому Timsort (вбудований у Python) найефективніший у більшості випадків.
"""

import random
import timeit
import matplotlib.pyplot as plt

# Insertion Sort
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Timsort (built-in)
def timsort(arr):
    return sorted(arr)

# Benchmark wrapper
def benchmark(func, data):
    return timeit.timeit(lambda: func(data), number=1)

def run_comparison():
    sizes = [100, 1000, 5000, 10000, 20000]
    results = {"Insertion Sort": [], "Merge Sort": [], "Timsort": []}

    for size in sizes:
        test_data = [random.randint(0, size) for _ in range(size)]
        results["Insertion Sort"].append(benchmark(insertion_sort, test_data))
        results["Merge Sort"].append(benchmark(merge_sort, test_data))
        results["Timsort"].append(benchmark(timsort, test_data))

    # Вивід результатів
    print("\nПорівняння часу виконання (в секундах):")
    print(f"{'Розмір':>10} | {'Insertion':>10} | {'Merge':>10} | {'Timsort':>10}")
    print("-" * 45)
    for i, size in enumerate(sizes):
        print(f"{size:>10} | {results['Insertion Sort'][i]:>10.5f} | {results['Merge Sort'][i]:>10.5f} | {results['Timsort'][i]:>10.5f}")

    # Побудова графіка
    plt.plot(sizes, results["Insertion Sort"], label="Insertion Sort")
    plt.plot(sizes, results["Merge Sort"], label="Merge Sort")
    plt.plot(sizes, results["Timsort"], label="Timsort")
    plt.xlabel("Кількість елементів")
    plt.ylabel("Час виконання (сек)")
    plt.title("Порівняння алгоритмів сортування")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sorting_comparison.png")
    plt.show()

if __name__ == "__main__":
    run_comparison()