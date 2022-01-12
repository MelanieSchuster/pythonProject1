
class BankError(Exception):
    pass

class AccountNotExistError(BankError):
    pass

class NotEnoughMoneyError(BankError):
    pass

class NegativeAmountError(BankError):
    pass

class Customer:
    last_id = 0

    # class-wide variable as num_rect in rectangle 6
    # single variable that shares all rectangles
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id
        # create an identifier: everytime we add a customer an ID will be added automatically

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.last_id, self.first_name, self.Customer.last_name, self.email)

class Account:
    last_id = 0

    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError('{0} amount provided to deposit {1}'.format(self.id, amount))
        else:
            self._balance =+ amount

    def charge(self, amount):
        if amount < 0:
            raise NegativeAmountError('{0} amount provided to deposit: {1}'.format(self.id, amount))
        if amount > self._balance:
            raise NotEnoughMoneyError('{0} amount provided to deposit: {1}'.format(self.id, amount))
        self._balance -= amount
        # Todo - add method 'charge' and 'deposit' that will change the balance
        # Homework: think about all the cases when something can go wron (not enough money...)
        # different data that the user could provide and how to add some logic that can handle that
        # negative sum: increase the balance instead of decreasing - handle these cases

    def __repr__(self):
        return 'Account[{},{},{}]'.format(self.__class__.__name__, self.id, self.last_name, self._balance)

class SavingsAccount(Account):
    interest_rate = 0.02

    def calc_interest(self):
        self._balance += self.interest_rate + self._balance


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []

    def new_customer(self, first_name, last_name, email):
        # TODO - create a new customer, add it to a list of customers
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c

    def new_account(self, customer, is_savings=True):
        # TODO - create a new account and add it to the list of accounts
        # if is_savings:
        #    a = SavingsAccount(customer)
        # else:
        #    a = CheckingAccount(customer)
        a = SavingsAccount(Customer) if is_savings else CheckingAccount(Customer)
        self.acc_list.append(a)
        return a

    def transfer(self, from_account_id, to_account_id, amount):
        from_acc = self.acc_list[from_account_id-1]
        to_acc = self.acc_list[to_account_id-1]
        from_acc.charge(amount)
        to_acc.deposit(amount)

    def __repr__(self):
        return 'Bank{}\n{}\n'.format(self.cust_list, self.acc_list)


b = Bank()

c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')

a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)

try:
    a1.deposit(100)
    a2.deposit(50)

    print(b)
    b.transfer(a1.id, a2.id, 80)
except BankError as be:
    print('Got error: {}'.format(be))
print(b)
