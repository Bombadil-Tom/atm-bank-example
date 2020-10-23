'''
test1:
    insert card
    insert card again
    shouldn't work

def test_validate_pin_without_card_inserted(self):
    atm = ATM()
    atm.validate_pin()

test2:
    validate pin
    shouldn't work because card was not inserted

test3:
    insert card
    input pin
    deposit 50
    check balance, balance should be 30
    end operation

    insert card
    input pin
    withdraw 20
    check balance, balance should be 30

'''

def validate_api(card_nr, pin):
    # validate account nr and pin
    # return true or fale
    return True

class Card:
    def __init__(self, accounts=None):
        self.accounts = accounts or []

    def select_account(self, account_nr):
        for account in self.accounts:
            if account.account_nr == account_nr:
                return account

        return None

class Account:
    def __init__(self, account_nr):
        self.account_nr = account_nr
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class ATM:
    def __init__(self):
        self.card_inserted = False
        self.card_validated = False
        self.current_account = None
        self.current_card = None

    def assert_is_validated(self):
        if self.card_inserted is False:
            raise RuntimeError('Card must be inserted first')

        if self.card_validated is False:
            raise RuntimeError("Card not validated")

    def insert_card(self, bank_card):
        # code to accept card
        self.card_inserted = True
        self.current_card = bank_card

    def eject_card(self):
        self.end_session()
        # code to push card out

    def validate_pin(self, pin):
        if self.card_inserted is False:
            raise RuntimeError('Card must be inserted first')

        # card is inserted, pin has to be validated
        # post pin and card number to api
        # response will be saved in validated variable

        self.card_validated = validate_api(card_nr=0,pin=0)

        return self.card_validated

    def select_account(self, account_nr):
        self.assert_is_validated()

        current_account = self.current_card.select_account(account_nr)
        self.current_account = current_account

    def perform_request(self, request, amount=0):
        '''
        1 = check balance
        2 = deposit money
        3 = withdraw money
        '''
        self.assert_is_validated()
        if request == 1:
            return self.check_balance()
        elif request == 2:
            return self.accept_cash(amount)
        elif request == 3:
            return self.give_out_cash(amount)
        else:
            raise RuntimeError("invalid request")

    def accept_cash(self, amount):
        # open cash tray
        # count cash
        self.current_account.deposit(amount)
        return amount

    def give_out_cash(self, amount):
        # count cash
        # open tray
        self.current_account.withdraw(amount)
        return amount

    def check_balance(self):
        return self.current_account.balance

    def end_session(self):
        self.card_inserted = False
        self.card_validated = False
        self.current_account = None
        self.current_card = None
        return True

def test_depositing_50_bucks_and_withdrawing_20():
    checking = Account(1)
    saving = Account(2)
    bank_card = Card([checking, saving])
    atm = ATM()

    atm.insert_card(bank_card)
    atm.validate_pin("123")
    atm.select_account(1)
    atm.perform_request(2, 50)
    if atm.perform_request(1) is not 50:
        raise Exception("depositing function doesn't work")
    atm.end_session()

    atm.insert_card(bank_card)
    atm.validate_pin("123")
    atm.select_account(1)
    atm.perform_request(3, 20)
    if atm.perform_request(1) is not 30:
        raise Exception("withdrawing function doesn't work")

    atm.select_account(2)
    atm.validate_pin("123")
    atm.perform_request(2, 10)

    if atm.perform_request(1) is not 10:
        raise Exception("depositing function doesn't work")

    print("Test successful")


if __name__ == "__main__":
    test_depositing_50_bucks_and_withdrawing_20()