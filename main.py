from src.utils import read_file
from src.app import find_cheapest_operator, create_trie

operator_a = read_file("data/operator_a.json")
operator_b = read_file("data/operator_b.json")
trie = create_trie(operator_a, operator_b)


def main(phone_num: str):
    return find_cheapest_operator(phone_num, trie)


if __name__ == "__main__":
    num = input("Insert a number: ")

    print(main(num))
