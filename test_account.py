import pytest
from account import *

class Test:
    def setup_method(self):
        self.p1 = Account('Jane')
        self.p2 = Account('John')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p1.get_balance() == pytest.approx(0, abs = 0.001)

        assert self.p2.get_name() == 'John'
        assert self.p2.get_balance() == pytest.approx(0, abs = 0.001)

    def test_deposit(self):
        # Basic deposit test
        assert self.p1.deposit(30) is True
        assert self.p1.get_balance() == pytest.approx(30, abs = 0.001)

        # Zero deposit test
        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(30, abs = 0.001)

        # Negative deposit test
        assert self.p1.deposit(-30) is False
        assert self.p1.get_balance() == pytest.approx(30, abs = 0.001)

    def test_withdraw(self):
        self.p1.deposit(30)

        # Basic withdraw test
        assert self.p1.withdraw(25) is True
        assert self.p1.get_balance() == pytest.approx(5, abs = 0.001)

        # Withdrawing beyond current account balance
        assert self.p1.withdraw(10) is False
        assert self.p1.get_balance() == pytest.approx(5, abs = 0.001)

        # Zero withdraw test
        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(5, abs = 0.001)

        # Negative withdraw test
        assert self.p1.withdraw(-10) is False
        assert self.p1.get_balance() == pytest.approx(5, abs = 0.001)

    def test_get_balance(self):
        assert self.p1.get_balance() == pytest.approx(0, abs = 0.001)
        self.p1.deposit(25.34)
        assert self.p1.get_balance() == pytest.approx(25.34, abs = 0.001)

    def test_get_name(self):
        assert self.p1.get_name() == 'Jane'
        assert self.p2.get_name() == 'John'