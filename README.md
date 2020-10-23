# atm-bank-example
This is a simple atm bank system design

I left out things like cash bin per atm and opening cash trays, etc. I also wanted to neglect APIs to validate pins, etc. (it's just a function that will always return `True`). I wanted to focus on classes and methods.

- Account class which has an account number, a balance and withdraw and deposit functions

- Card class which has accounts and a select account function which will search for the account number on the card and then return it

- ATM class which has the following variables: `card_inserted`, `card_validated`, `current_account`, `current_card` and the main function are `perform_request` (which will either give out the balance, deposit or withdraw money), `validate_pin` (which will make the call to the API, mocked in my code), `select_account` (which will select an account from the card)

