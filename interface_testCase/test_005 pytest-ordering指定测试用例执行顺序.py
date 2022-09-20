import pytest


class TestLogin:
    @pytest.mark.run(order=1)
    def test_aaa(self):
        print("test_aaa")

    @pytest.mark.run(order=3)
    def test_bbb(self):
        print("test_bbb")

    @pytest.mark.run(order=2)
    def test_ccc(self):
        print("test_ccc")
