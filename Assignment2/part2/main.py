import knapsack01 as k01
import knapsack_fractional as kf
from random import shuffle


def knapsack_program_user():
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

def knapsack_program(weights: list, values: list, capacity: int, amount: int):
    print("Item indexes start with 1")

    for x in range(amount):
        shuffle(weights)
        shuffle(values)

        print(f"\nProblem #{x+1}")
        print(f"Values: {values}")
        print(f"Weights: {weights}")

        k01.input_wrapper(weights, values, capacity)
        kf.input_wrapper(weights, values, capacity)


# cap = 100
# values = [120, 200, 240]
# weights = [20, 40, 60]
if __name__ == '__main__':
    amount = 3

    cap = 100
    values = [120, 200, 240, 10, 55, 72]
    weights = [20, 40, 60, 10, 80, 35]

    knapsack_program(weights, values, cap, amount)

    #while True:
        #knapsack_program_user()

