import unittest

from ATM import Account, ATM, Card

class TestAccount(unittest.TestCase):
    def setUp(self):
        checking = Account(101)
        saving = Account(102)
        self.bank_card = Card([checking, saving])
        self.atm = ATM()
        self.checking = checking
        self.saving = saving

    def deposit_50(self):
        self.atm.perform_request(2,50)

    def withdraw_20(self):
        self.atm.perform_request(3,20)

    def test_account_starts_with_0(self):
        self.assertEqual(self.checking.balance, 0)
        self.assertEqual(self.saving.balance, 0)

    def test_deposit(self):
        atm = self.atm
        bank_card = self.bank_card

        atm.insert_card(bank_card)
        atm.validate_pin("123")
        atm.select_account(101)
        self.deposit_50()

        balance = self.checking.balance
        self.assertEqual(balance, 50)

    def test_withdraw(self):
        atm = self.atm
        bank_card = self.bank_card

        atm.insert_card(bank_card)
        atm.validate_pin("123")
        atm.select_account(102)
        self.withdraw_20()

        balance = self.saving.balance
        self.assertEqual(balance, -20)


    def test_deposit_50_and_withdraw_20(self):
        atm = self.atm
        bank_card = self.bank_card

        atm.insert_card(bank_card)
        atm.validate_pin("123")
        atm.select_account(101)
        atm.perform_request(2, 50)

        balance = atm.perform_request(1)
        self.assertEqual(balance, 50)

        atm.eject_card()

        atm.insert_card(bank_card)
        atm.validate_pin("123")
        atm.select_account(101)
        atm.perform_request(3, 20)
        if atm.perform_request(1) is not 30:
            raise Exception("withdrawing function doesn't work")

        atm.select_account(102)
        atm.validate_pin("123")
        atm.perform_request(2, 10)
        balance = atm.perform_request(1)
        self.assertEqual(balance, 10)

    def test_withdraw_without_pin_throws_error(self):
        atm = self.atm
        bank_card = self.bank_card

        atm.insert_card(bank_card)

        with self.assertRaises(RuntimeError) as e:
            atm.select_account(101)
            self.assertEqual(type(e.exception), RuntimeError)


if __name__ == "__main__":
    unittest.main()