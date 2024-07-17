from src.app import find_cheapest_operator, create_trie


class TestApp:
    def test_wrong_number(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"93": 0.50, "358": 0.69, "355": 0.48}
        trie = create_trie(a, b)
        res = find_cheapest_operator("93a456", trie)
        assert res == "Wrong number"

    def test_same_item_list(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"93": 0.50, "358": 0.69, "355": 0.48}
        trie = create_trie(a, b)

        res = find_cheapest_operator("934756475", trie)
        assert res == ("A", 0.46)

    def test_different_item_list(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"358": 0.69, "355": 0.48}
        trie = create_trie(a, b)

        res = find_cheapest_operator("934756475", trie)
        assert res == ("A", 0.46)

    def test_not_found_phone_num(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"93": 0.50, "358": 0.69, "355": 0.48}
        trie = create_trie(a, b)

        res = find_cheapest_operator("0589317381", trie)

        assert res == ("Empty", None)

    def test_return_one_digit_prefix(self):
        a = {"1": 0.46, "122": 0.69, "124": 0.48}
        b = {"93": 0.50}
        trie = create_trie(a, b)

        res = find_cheapest_operator("123456789", trie)
        assert res == ("A", 0.46)

    def test_return_longest_prefix(self):
        a = {"1": 0.46, "122": 0.69, "1224": 0.48, "122456": 0.2}
        b = {"93": 0.50, "358": 0.69, "355": 0.48, "122456": 0.3}
        trie = create_trie(a, b)

        res = find_cheapest_operator("122456789", trie)
        assert res == ("A", 0.2)

    def test_create_trie(self):
        a = {"1": 0.46, "122": 0.69, "1224": 0.48, "122456": 0.2}
        b = {"93": 0.50, "358": 0.69, "355": 0.48, "122456": 0.3}

        res = create_trie(a, b)
        assert res.root.children["1"].price == 0.46
