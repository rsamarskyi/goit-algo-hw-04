import timeit
import random

def insertion_sort(data: list[int]) -> list[int]:
    result = data.copy()

    for i in range (1, len(data)):
        current = result[i]
        j = i - 1
        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current

    return result

def merge_sort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data.copy()
    else:
    
        middle = len(data) // 2
        left = merge_sort(data[:middle])
        right = merge_sort(data[middle:])

        return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main() -> None:
    datasets = {}

    for size in (1000, 2000, 4000):
        random.seed(42)
        datasets[f"Випадкові, {size}"] = [
            random.randint(0, 10000) for _ in range(size)
        ]

    datasets["Відсортовані, 4000"] = list(range(4000))
    datasets["Зворотний порядок, 4000"] = list(range(4000, 0, -1))

    algorithms = {
        "Insertion sort": insertion_sort,
        "Merge sort": merge_sort,
        "Timsort (sorted)": sorted,
    }

    repetitions = 10

    for dataset_name, data in datasets.items():
        print(f"\n{dataset_name}")

        expected = sorted(data)

        for algorithm_name, algorithm in algorithms.items():
            # Перевіряємо правильність поза вимірюванням часу
            assert algorithm(data) == expected, (
                f"Помилка сортування: {algorithm_name}"
            )

            elapsed = timeit.timeit(
                lambda: algorithm(data),
                number=repetitions,
            )

            print(
                f"{algorithm_name}: "
                f"{elapsed / repetitions:.6f} с"
            )


if __name__ == "__main__":
    main()