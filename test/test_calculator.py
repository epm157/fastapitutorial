from app.calculator import add, BankAccount, BalanceException
import pytest

def test_add():
    print("testing add from calculator")
    result = add(1, 2)
    assert result == 3

@pytest.mark.parametrize("num1, num2, expected", [(3, 2, 5), (1, 2, 3)])
def test_add_parametrized(num1, num2, expected):
    print("testing add from calculator")
    result = add(num1, num2)
    assert result == expected

def test_bank_account1():
    acc = BankAccount()
    assert acc.balance == 0

@pytest.mark.parametrize("balance, expected", [(3, 3), (1, 1)])
def test_bank_account2(balance, expected):
    acc = BankAccount(balance)
    assert acc.balance == expected


@pytest.fixture
def zero_bank_account():
    return BankAccount

@pytest.fixture
def bank_account():
    return BankAccount(50)


def test_bank_account3(bank_account):
    assert bank_account.balance == 50

@pytest.mark.parametrize("amount, expected", [(4, 54), (5, 55)])
def test_bank_account3(bank_account, amount, expected):
    bank_account.deposit(amount)
    assert bank_account.balance == expected

def test_bank_account3(bank_account):
    with pytest.raises(BalanceException):
        bank_account.withdraw(300)

















