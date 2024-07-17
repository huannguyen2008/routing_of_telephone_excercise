class Operator:
    A = "A"
    B = "B"


class _TrieNode:
    def __init__(self, operator: str = ""):
        self.children = dict()
        self.is_end = False
        self.price = 0
        self.operator = operator


class Trie:
    def __init__(self):
        self.root = _TrieNode()

    def insert(self, phone_prefix: str, price: float, operator: str) -> None:
        cur = self.root

        for n in phone_prefix:
            if n not in cur.children:
                cur.children[n] = _TrieNode(operator=cur.operator)
            cur = cur.children[n]
        cur.is_end = True
        if price < cur.price or not cur.price:
            cur.price = price
            cur.operator = operator

    def search(self, phone_num: str) -> str:
        cur = self.root

        for n in phone_num:
            if not n.isdigit():
                return "Wrong number"
            elif n not in cur.children:
                if cur.is_end:
                    return cur.operator
                else:
                    return "Not found" if not cur.operator else cur.operator
            cur = cur.children[n]

    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + key + (f"---{child.price}" + f"---{child.operator}") + ("$" if child.is_end else "")
                           + recur(child, indent + "  ")
                           for key, child in node.children.items())

        return recur(self.root, "\n")
