class _TrieNode:
    def __init__(self, operator: str = "Empty"):
        self.children = dict()
        self.is_end = False  # to check whether the prefix is end when inserting
        self.price = None
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
        if not cur.price or price < cur.price:
            cur.price = price
            cur.operator = operator

    def search(self, phone_num: str) -> (str, any):
        cur = self.root
        price = None
        operator = "Empty"

        for n in phone_num:
            if not n.isdigit():
                return "Wrong number"

            if n not in cur.children:
                return operator, price

            cur = cur.children[n]

            if cur.is_end:
                price = cur.price
                operator = cur.operator

        return operator, price

    def __repr__(self):
        """
        Use a recursive function to print the Trie for debugging
        Example:
        4---None---Empty
            3---0.05---B$
                4---None---Empty
                    5---0.7---A$
        :return:
        """
        def recur(node, indent):
            return "".join(indent + key + (f"---{child.price}" + f"---{child.operator}") + ("$" if child.is_end else "")
                           + recur(child, indent + "  ")
                           for key, child in node.children.items())

        return recur(self.root, "\n")
