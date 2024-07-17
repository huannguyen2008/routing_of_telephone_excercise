import json
import random


def read_file(file_name: str):
    with open(file_name) as file:
        data = json.load(file)
    return data


def write_to_file(data: dict, file_name: str):
    with open(file_name, "w") as file:
        json.dump(data, file)


def remove_random_data(num: int, data: list):
    for i in range(0, num):
        random_element = random.choice(data)
        data.remove(random_element)
    return data


def random_float(digits: int):
    return round(random.uniform(0, 1), digits)
