from src.trie import Trie


def find_cheapest_operator(phone_num: str, data_a: dict, data_b: dict):
    trie = Trie()

    for k, v in data_a.items():
        trie.insert(phone_prefix=k, price=v, operator="A")

    for k, v in data_b.items():
        trie.insert(phone_prefix=k, price=v, operator="B")
    print(trie)
    return trie.search(phone_num)
