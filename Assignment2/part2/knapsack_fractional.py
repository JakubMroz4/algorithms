
class Item:
    def __init__(self, value, weight, id):
        self.value = value
        self.weight = weight
        self.id = id

    def ratio(self):
        return self.value / self.weight


def fractional_knapsack(items: list, capacity: int):
    # sort by value / weight ratio, decreasingly
    items.sort(key=lambda x: x.ratio(), reverse=True)
    max_value = 0.0
    solution_items = []

    if capacity == 0:
        return 0, list()

    # iterate over items
    for index, item in enumerate(items):

        # try to add entire item
        if item.weight <= capacity:
            capacity -= item.weight
            max_value += item.value
            solution_items.append(item.id)

        # else add fraction of it
        else:
            max_value += item.value * capacity / item.weight
            solution_items.append(item.id)
            break
            
    return max_value, solution_items

def input_wrapper(weight_list, value_list, capacity):
    assert len(weight_list) == len(value_list)
    assert capacity >= 0

    items = []
    for x in range(len(weight_list)):
        items.append(Item(value_list[x], weight_list[x], x + 1))

    solution, solution_items_list = fractional_knapsack(items, capacity)

    print("\nFractional Knapsack")
    print(f"Solution: {solution}")
    print(f"Items in the solution: {solution_items_list}")


if __name__ == "__main__":
    capacity = 100
    items = [Item(120, 200, 1), Item(120, 20, 2), Item(200, 40, 3), Item(240, 60, 4), Item(70, 10, 5)]

    solution, solution_items_list = fractional_knapsack(items, capacity)

    print("\nFractional Knapsack")
    print(f"Solution: {solution}")
    print(f"Items in the solution: {solution_items_list}")