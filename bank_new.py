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
        self.pin = "1234"

    # add methods "charge" and "deposit" that will change the balance
    # validation system
    def checkPin(self, pin):
        if self.pin == pin:
            return True
        else:
            return False

    # Function to make a deposit
    def deposit(self, pin, amount):
        pin = input("\n Please Enter pin code: ")
        if self.checkPin(pin) is True:
            self._balance += amount
            print("\n Amount Deposited", amount)
        else:
            print("\n Wrong Pin. Please try again.")

    # Function that will make a charge
    def charge(self, pin, amount):
        pin = input("\n Please Enter pin code: ")
        if self.checkPin(pin) is True:
            if amount <= self._balance:
                self._balance -= amount
                print("\n You Withdrew from the account: ", amount)
            else:
                print("\n Not enough money on that account")
        else:
            print("\n Wrong pin code. Please try again.")

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self._balance)

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
        #create a new account and add it to the list of accounts
        # if is_savings:
        #     a = SavingsAccount(customer)
        # else:
        #     a = CheckingAccount(customer)
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        self.acc_list.append(a)
        return a
    def transfer(self, from_account_id, to_account_id, amount):
        from_account_id.charge(amount, amount)
        to_account_id.deposit(amount, amount)
        pass
    # validation of IBAN
        #TODO - please note that you might need to find the "from" and "to" accounts in the list
        # based on the ids provided as input
    #if ID is in dict, dann mach die transaktion, ansonsten print "wrong ID" oder so
    def __repr__(self):
        return 'Bank\n{}\n{}'.format(self.cust_list, self.acc_list)

b = Bank()
c1 = b.new_customer('John', 'Brown', 'john@brown.com')
c2 = b.new_customer('Anna', 'Smith', 'anne@smith.com')
a1 = b.new_account(c1, is_savings=True)
a2 = b.new_account(c1, is_savings=False)

a = Account(c1)
a.checkPin(c1)
a.deposit(c1, 2500)
a.charge(c1, 100)


a2 = Account(c2)
a2.checkPin(c2)
a2.deposit(c2, 300)
a2.charge(c2, 100)

b.transfer(a, a2, 20)

print(b)
print(a)
print(a2)