

def knapsack_01(weights: list, values: list, capacity: int):
    length = len(weights)

    # create 2d array Capacity + 1 x Items + 1
    # last value in matrix[i] will be max value for the last i items
    matrix = [[0 for _ in range(capacity + 1)] for _ in range(length + 1)]

    # iterate over items
    for i in range(1, length + 1):
        # iterate over weights
        for w in range(1, capacity + 1):

            # if next items does not exceed capacity
            # choose max of not including the item or including the item
            if weights[i - 1] <= w:
                matrix[i][w] = max(matrix[i - 1][w], values[i - 1] + matrix[i - 1][w - weights[i - 1]])

            # if capacity exceeded: do not include the item
            else:
                matrix[i][w] = matrix[i - 1][w]

    max_value = matrix[length][capacity]
    return max_value, matrix

def solution_items(weights: list, matrix: list):
    length = len(weights)
    capacity = len(matrix[0]) - 1
    solution_items = []

    while length > 0 and capacity > 0:
        if matrix[length][capacity] != matrix[length - 1][capacity]:
            solution_items.append(length)
            capacity -= weights[length - 1]

        length -= 1

    solution_items = sorted(solution_items)
    return solution_items


def input_wrapper(weight_list, value_list, capacity):
    assert len(weight_list) == len(value_list)
    assert capacity >= 0

    solution, matrix = knapsack_01(weight_list, value_list, capacity)
    solution_items_list = solution_items(weight_list, matrix)
    print("\n01 Knapsack")
    print(f"Solution: {solution}")
    print(f"Items in the solution: {solution_items_list}")


if __name__ == '__main__':
    values = [120, 200, 240]
    weights = [20, 40, 60]
    W = 100

    solution, matrix = knapsack_01(weights, values, W)
    solution_items_list = solution_items(weights, matrix)
    print(solution)
    print(solution_items_list)