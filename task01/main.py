import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from measure_time import measure_time


def generate_data(size):
    return [random.randint(0, 1000000) for _ in range(size)]

def main():
    data_sizes = [100, 10000, 50000]

    for size in data_sizes:
        print(f"\nData size: {size}")
        data = generate_data(size)

        # Timsort
        python_sort_time = measure_time(lambda d: d.sort(), data.copy())
        print(f"Python Timsort: {python_sort_time:.6f} seconds")

        # Insertion Sort
        insertion_sort_time = measure_time(insertion_sort, data.copy())
        print(f"Insertion Sort: {insertion_sort_time:.6f} seconds")

        # Merge Sort
        merge_sort_time = measure_time(merge_sort, data.copy())
        print(f"Merge Sort: {merge_sort_time:.6f} seconds")


if __name__ == "__main__":
    main()
