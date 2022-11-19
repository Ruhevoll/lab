


class Account:

    def __init__(self, name: str) -> None:
        """
        Function to create a bank account.

        :param name: Name of the bank account.
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to deposit funds into a bank account.

        :param amount: Amount to be deposited.
        :return: Whether deposit was successful.
        """
        if amount > 0:
            self.__account_balance = self.__account_balance + amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to withdraw funds from a bank account.

        :param amount: Amount to be withdrawn.
        :return: Whether withdrawal was successful.
        """
        if (amount <= self.__account_balance) and (amount > 0):
            self.__account_balance = self.__account_balance - amount
            return True
        else:
            return False

    def get_balance(self) -> float:
        """
        Get the balance of a bank account.

        :return: The balance of the bank account.
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Get the name of a bank account.

        :return: The name of the bank account.
        """
        return self.__account_name

