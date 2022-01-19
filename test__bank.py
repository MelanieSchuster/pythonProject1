import random

class Customer:
    last_id = 0
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)

class Account:
    last_id = 0
    def __init__(self, customer):
        Account.last_id += 1
        self.id = Account.last_id
        self.customer = customer
        self._balance = 0
        self.pin = str(random.randint(999, 9999))

    # Validation
    def checkPin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    # Deposit
    def deposit(self, pin, amount):
            self._balance += amount
            print("\n You Deposited:", amount)

    # Charge
    def charge(self, pin, amount):
        pin = input("\n Please Enter pin: ")
        if self.checkPin(pin) is True:
            if amount <= self._balance:
                self._balance -= amount
                print("\n You Withdrew: ", amount)
            else:
                print("\n Account balance not covered.")
        else:
            print("\n Wrong pin. Please try again.")

    def __repr__(self):
        return '{}[{},{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self.pin, self._balance)

class SavingsAccount(Account):
    interest_rate = 0.02
    def calc_interest(self):
        self._balance += self.interest_rate * self._balance

class CheckingAccount(Account):
    pass

class Bank:
    def __init__(self):
        self.cust_list = []
        self.acc_list = []
    def new_customer(self, first_name, last_name, email):
        #create a new customer, add it to a list of customers
        c = Customer(first_name, last_name, email)
        self.cust_list.append(c)
        return c
    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a
    def transfer(self, from_account_id, to_account_id, amount):
        from_account_id.charge(amount, amount)
        to_account_id.deposit(amount, amount)
        pass
    def _repr_(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()
c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c2, is_savings=False)

# initial balances
print("The initial balances are: ", a1, a2)

# deposit and charge on account 1
print("Your Customer and Account Data: ", c1, a1)
a1.deposit(c1, 2500)
a1.charge(c1, 100)

# deposit and charge on account 2
print("Your Customer and Account Data: ", c2, a2)
a2.deposit(c2, 300)
a2.charge(c2, 200)

# transfer from account 1 to account 2
print("The accounts involved in this transfer are: ", a1, a2)
b.transfer(a1, a2, 300)


# resulting balances
print("The resulting balances are: ", a1, a2)