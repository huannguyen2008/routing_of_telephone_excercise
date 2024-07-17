from src.trie import Trie


def create_trie(data_a: dict, data_b: dict):
    trie = Trie()

    for k, v in data_a.items():
        trie.insert(phone_prefix=k, price=v, operator="A")

    for k, v in data_b.items():
        trie.insert(phone_prefix=k, price=v, operator="B")
    print(trie.root.children)
    return trie


def find_cheapest_operator(phone_num: str, trie: Trie):
    return trie.search(phone_num)
