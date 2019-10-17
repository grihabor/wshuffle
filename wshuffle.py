from collections import Counter
from random import expovariate
from typing import NamedTuple


class Item(NamedTuple):
    key: float
    value: int


def weighted_shuffle(arr, weights):
    items = [
        Item(key=expovariate(weight), value=arr_item)
        for weight, arr_item in zip(weights, arr)
    ]
    return [item.value for item in sorted(items, key=lambda item: item.key)]


def main():
    weights = [3, 5, 2]
    arr = ["a", "b", "c"]
    first_place_counter = Counter(
        weighted_shuffle(arr, weights)[0] for _ in range(10000)
    )
    print(first_place_counter)


if __name__ == "__main__":
    main()
