import knapsack01 as k01
import knapsack_fractional as kf


def knapsack_program():
    print("Knapsack problem program")
    index = 1

    values = []
    weights = []

    capacity = int(input("Knap capacity: "))

    while True:
        print(f"\nItem #{index}")
        print(f"(Press enter to stop item input)")
        value = input("Item value: ")
        if not value.isnumeric():
            break

        weight = input("Item weight: ")
        if not weight.isnumeric():
            break

        values.append(int(value))
        weights.append(int(weight))

        index += 1

    print()
    print(f"Capacity: {capacity}")
    print(f"Values: {values}")
    print(f"Weights: {weights}")

    k01.input_wrapper(weights, values, capacity)
    kf.input_wrapper(weights, values, capacity)


# cap = 100
# values = [120, 200, 240]
# weights = [20, 40, 60]
if __name__ == '__main__':
    while True:
        knapsack_program()
