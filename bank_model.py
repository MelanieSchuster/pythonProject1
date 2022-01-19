# install sqlalchemy before

from sqlalchemy import Column, Integer, String, ForeignKey, Float, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
#basis for all clasis that will represent that tables

class BankError(Exception):
    pass

class AccountNotExistsError(BankError):
    pass

class NotEnoughMoneyError(BankError):
    pass

class NegativeAmountError(BankError):
    pass


class Customer(Base):
# create a customer table (inherits from base)
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    # automatically get updated
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(80))
    accounts = relationship('Account', back_populates="customer")
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    bank = relationship('Bank', lazy='select', back_populates='customers')
# this is a column and how it should be
# nullable = False -> it is obligatory
# specified under the class: called class-variables
# they work as a class-wide / shared variable
# no value: reference to a column for all the data

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    # instance variable, a variable inside an object (when there is a self.)
# different for every last name

    def __repr__(self):
        return 'Customer[{},{},{},{}]'.format(self.id, self.first_name, self.last_name, self.email)


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True, autoincrement=True)
    balance = Column(Float)
    fk_customer_id = Column(Integer, ForeignKey(Customer.id), index=True, nullable=False)
    # specifies that it is a foreign key to the id above
    customer = relationship(Customer, back_populates='accounts')
    type = Column(String(20))
    fk_bank_id = Column(Integer, ForeignKey('bank.id'), index=True, nullable=False)
    # what does nullable = false mean on a foreign key?
    # this value cannot be left empty: we have to specify the owner everytime we create an account
    # we can not have accounts that not belong to anyone
    bank = relationship('Bank', lazy='select', back_populates='accounts')
    #every account has a relationship to a bank, using the foreign key
    __mapper_args__ = {
        'polymorphic_identity': 'account',
        'polymorphic_on': type
    }
    # if we create an object of account, the type is account
    # if we create a saving account, it will be saving account
    # type shows which account we have

    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

    # TODO - add methods "charge" and "deposit" that will change the balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('New deposit updated as: {}'.format(self.balance))
        else:
            raise NegativeAmountError('The amount is negative')

    def charge(self, amount):
        if amount > self.balance:
            raise NotEnoughMoneyError(
                "You don't have enough Balance. Your Current Balance is {}".format(self.balance)
                , self.balance)
        if amount <= 0:
            raise NegativeAmountError("The amount is negative. Please input the positive amount")
        else:
            self.balance -= amount
            print("Charge amount is: {}".format(amount))
            print("New Balance updated as: {}".format(self.balance))

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.last_name, self.balance)


class SavingsAccount(Account):
    __tablename__ = 'savings_account'
    id = Column(Integer, ForeignKey(Account.id), primary_key=True)
    # the table will contain the id of the account as a foreign key which is also the primary key
    interest_rate = Column(Float)

    __mapper_args__ = {
        'polymorphic_identity': 'savings_account',
    }

    def calc_interest(self):
        self.balance += self.interest_rate * self.balance


class CheckingAccount(Account):
    __tablename__ = 'checking_account'
    id = Column(Integer, ForeignKey(Account.id), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'checking_account',
    }


class Bank(Base):
    __tablename__ = 'bank'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    customers = relationship(Customer, cascade='all, delete-orphan, delete', lazy='select')
    accounts = relationship(Account, cascade='all, delete-orphan, delete', lazy='select')

    def __init__(self, name):
        self.name = name

    def new_customer(self, first_name, last_name, email):
        c = Customer(first_name, last_name, email)
        c.fk_bank_id = self.id
        return c

    def new_account(self, customer, is_savings=True):
        a = SavingsAccount(customer) if is_savings else CheckingAccount(customer)
        a.fk_bank_id = self.id
        return a

    def _find_acc_by_id(self, acc_id):
        for acc in self.accounts:
            if acc.id == acc_id:
                return acc
        return None

    def transfer(self, from_account_id, to_account_id, amount):
        from_acc = self._find_acc_by_id(from_account_id)
        to_acc = self._find_acc_by_id(to_account_id)
        from_acc.charge(amount)
        to_acc.deposti(amount)

    def __repr__(self):
        return 'Bank[{}]:\n{}\n{}'.format(self.name, self.customers, self.accounts)

# below here: code that is necessary to connect to the database

class DBSession:
    current_db_session = None

    def engine(self):
        url = 'sqlite:///bank.db'
        return create_engine(url, echo=True)
    # connects to database
    # this is the only part that changes if you imigrate to another database

    def db_session(self):
        """Opens a new database connection if there is none yet for the
        current application context.
        """
        if not DBSession.current_db_session:
            Session = sessionmaker(bind=self.engine(), autocommit=False, autoflush=False)
            current_db_session = Session()
        return current_db_session
    #check if db session has the current db session
    #autoflush: whether the data should be send automatically to the database engine
    #doesn't mean that it is automatically commited
    #autocommit to true is that it will be directly commited: no transactions that are manually specified
    # if you want to use transactions: autocommit = false

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    db_session = DBSession()
    Base.metadata.create_all(bind=db_session.engine())
    pass
# run just once
# but if you run it again it won't delete the existing tables