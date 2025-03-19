import random


def generate_random_number(min_value: int, max_value: int):
    return random.randint(min_value, max_value)

def choose_items(list_of_items: list, number_of_items_to_choose: int):
    return random.choices(list_of_items, k=number_of_items_to_choose)




