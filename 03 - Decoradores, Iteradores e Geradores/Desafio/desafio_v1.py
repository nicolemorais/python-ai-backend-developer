import functools
import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


class IteratorAccount:
    def __init__(self, accounts):
        self.accounts = accounts
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.accounts):
            return self.accounts[self.index]
        else:
            raise StopIteration


class Customer:
    def __init__(self, address):
        self.address = address
        self.accounts = []
        self.account_index = 0

    def perform_transaction(self, account, transaction):
        if len(account.history.day_transactions()) >= 2:
            print("Number of transactions exceeded today.")
            return False

        transaction.register(account)
        return True

    def add_account(self, account):
        self.accounts.append(account)


class Person(Customer):
    def __init__(self, name, birth, cpf, address):
        super().__init__(address)
        self.name = name
        self.birth = birth
        self.cpf = cpf


class BankAccount:
    def __init__(self, number, customer):
        self._balance = 0
        self._number = number
        self._branch = "0001"
        self._customer = customer
        self._history = History()

    @classmethod
    def new_account(cls, customer, number):
        return cls(number, customer)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def branch(self):
        return self._branch

    @property
    def customer(self):
        return self._customer

    @property
    def history(self):
        return self._history

    def withdrawal(self, amount):
        balance = self.balance
        exceeded_balance = amount > balance

        if exceeded_balance:
            self._balance -= amount
            print("\nOPERATION FAILED: Insufficient balance.")

        elif amount > 0:
            self._balance -= amount
            print("\nSUCCESS: Withdrawal made!")
            return True

        else:
            print("\nOPERATION FAILED: Entered amount is invalid.")

        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("\nSUCCESS: Deposit made!")

        else:
            print("\nOPERATION FAILED: Entered amount is invalid.")
            return False

        return True


class CurrentAccount(BankAccount):
    def __init__(self, number, customer, limit=500, withdrawal_limits=3):
        super().__init__(number, customer)
        self.limit = limit
        self.withdrawal_limits = withdrawal_limits

    def withdrawal(self, amount):
        number_checks = len(
            [transaction for transaction in self.history.transactions if
             transaction["type"] == Withdrawal.__name__])

        exceeded_limit = amount > self.limit
        exceeded_checks = number_checks >= self.withdrawal_limits

        if exceeded_limit:
            print("\nOPERATION FAILED: The withdrawal amount exceeds the limit. ")

        elif exceeded_checks:
            print("\nOPERATION FAILED: maximum number of withdrawals exceeded.")

        else:
            return super().withdrawal(amount)

        return False

    def __str__(self):
        return f"""
            Branch:\t{self.branch}
            C/C:\t{self.number}
            Owner:\t{self.customer.name}
        """


class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "current_time": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
        )

    def generate_report(self, transaction_type=None):
        for transaction in self.transactions:
            if transaction_type is None or transaction["type"].lower() == transaction_type.lower():
                yield transaction

    def day_transactions(self):
        current_date = datetime.now().date()
        transactions = [transaction for transaction in self.transactions if
                        datetime.strptime(transaction["current_time"], "%d-%m-%Y %H:%M:%S").date() == current_date]
        return transactions


class Transaction(ABC):
    @property
    @abstractproperty
    def amount(self):
        pass

    @abstractmethod
    def register(self, account):
        pass


class Withdrawal(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        success_transaction = account.withdrawal(self._amount)

        if success_transaction:
            account.history.add_transaction(self)


class Deposit(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account):
        success_transaction = account.deposit(self._amount)

        if success_transaction:
            account.history.add_transaction(self)


def log_transaction(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}: {func.__name__.upper()}")
        return result
    return wrapper


def menu():
    menu = """\n
    ================ MAIN ================
    [1]\tDeposit
    [2]\tWithdraw
    [3]\tStatement
    [4]\tNew customer
    [5]\tNew account
    [6]\tList accounts
    [0]\tQuit
    => """
    return input(textwrap.dedent(menu))


def filter_customer(cpf, costumers):
    filtered_customers = [customer for customer in costumers if customer.cpf == cpf]
    return filtered_customers[0] if filtered_customers else None


def recover_customer_account(customer):
    if not customer.accounts:
        print("\nOPERATION FAILED: No accounts found.")
        return

    return customer.accounts[0]


@log_transaction
def deposit(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\nOPERATION FAILED: No customer found.")
        return

    amount = float(input("Enter the amount to deposit: "))
    transaction = Deposit(amount)

    account = recover_customer_account(customer)
    if not account:
        return
    customer.perform_transaction(account, transaction)


@log_transaction
def withdrawal(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\nOPERATION FAILED: No customer found.")
        return

    amount = float(input("Enter the amount to withdraw: "))
    transaction = Withdrawal(amount)

    account = recover_customer_account(customer)
    if not account:
        return

    customer.perform_transaction(account, transaction)


@log_transaction
def display_statement(customers):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\nOPERATION FAILED: No customer found.")
        return

    account = recover_customer_account(customer)
    if not account:
        return

    print("\n======================= EXTRATO =======================")
    statement = " "
    has_transaction = False
    for transaction in account.history.generate_report():
        has_transaction = True
        statement += f"\n{transaction['current_time']}\n{transaction['type']}:\n\tR${transaction['amount']:.2f}"

    if not has_transaction:
        statement = "No activity was recorded."

    print(statement)
    print(f"\nBalance:\n\tR${account.balance:.2f}")
    print("=======================================================")


@log_transaction
def new_customer(customers):
    cpf = input("Enter the customer's CPF (numbers only): ")
    customer = filter_customer(cpf, customers)

    if customer:
        print("\nOPERATION FAILED: There is already a user registered with this CPF.")
        return

    name = input("Enter the customer's name: ")
    birth = input("Enter the customer's birth (dd-mm-yyyy): ")
    address = input("Enter the customer's address (Street name, Street number - Neighborhood, "
                    "City, State abbreviation): ")

    customer = Person(name=name, birth=birth, cpf=cpf, address=address)

    customers.append(customer)

    print("\nSUCCESS: New customer registered.")


@log_transaction
def new_account(number_account, customers, accounts):
    cpf = input("Enter the customer's CPF: ")
    customer = filter_customer(cpf, customers)

    if not customer:
        print("\nOPERATION FAILED: No customer found.")
        return

    account = CurrentAccount.new_account(customer=customer, number=number_account)
    accounts.append(account)
    customer.accounts.append(account)

    print("\nSUCCESS: New account created!")


def list_accounts(accounts):
    for account in accounts:
        print("-" * 100)
        print(textwrap.dedent(str(account)))


def main():
    customers = []
    accounts = []

    while True:
        option = menu()

        if option == '1':
            deposit(customers)

        elif option == '2':
            withdrawal(customers)

        elif option == '3':
            display_statement(customers)

        elif option == '4':
            new_customer(customers)

        elif option == '5':
            number_account = len(accounts) + 1
            new_account(number_account, customers, accounts)

        elif option == '6':
            list_accounts(accounts)

        elif option == '0':
            break

        else:
            print("\nOPERATION FAILED: Invalid option.")


main()
