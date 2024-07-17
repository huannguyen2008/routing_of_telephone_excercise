from src.app import find_cheapest_operator


class TestApp:
    def test_same_item_list(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"93": 0.50, "358": 0.69, "355": 0.48}
        res = find_cheapest_operator("934756475", a, b)
        assert res == "A"

    def test_different_item_list(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"358": 0.69, "355": 0.48}
        res = find_cheapest_operator("934756475", a, b)
        assert res == "A"

    def test_not_found_phone_num(self):
        a = {"93": 0.46, "358": 0.69, "355": 0.48}
        b = {"93": 0.50, "358": 0.69, "355": 0.48}
        res = find_cheapest_operator("9589317381", a, b)
        assert res == "Not found"

    def test_one_digit_prefix(self):
        a = {"1": 0.46, "122": 0.69, "124": 0.48}
        b = {"93": 0.50}
        res = find_cheapest_operator("123456789", a, b)
        assert res == "A"

    def test_longest_prefix(self):
        a = {"1": 0.46, "122": 0.69, "1224": 0.48, "122456": 0.2}
        b = {"93": 0.50, "358": 0.69, "355": 0.48, "122456": 0.3}
        res = find_cheapest_operator("122456789", a, b)
        assert res == "A"
