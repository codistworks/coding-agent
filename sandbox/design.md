### System Design
The system will consist of a single backend module `account_management.py` and a Gradio app `app.py`. The `account_management.py` module will contain the business logic for the account management system, while the `app.py` will provide a user interface to interact with the system.

#### Backend Module (`account_management.py`)
The backend module will contain the following classes and functions:

* `Account` class:
	+ `__init__(self, balance: float)`: Initializes an account with a given balance.
	+ `deposit(self, amount: float)`: Deposits a given amount into the account.
	+ `withdraw(self, amount: float)`: Withdraws a given amount from the account, if possible.
	+ `buy_shares(self, symbol: str, quantity: int)`: Buys a given quantity of shares of a given symbol, if affordable.
	+ `sell_shares(self, symbol: str, quantity: int)`: Sells a given quantity of shares of a given symbol, if available.
	+ `get_holdings(self)`: Returns the current holdings of the account.
	+ `get_portfolio_value(self)`: Returns the current total value of the account's portfolio.
	+ `get_profit_loss(self)`: Returns the current profit or loss of the account.
	+ `get_transaction_history(self)`: Returns the transaction history of the account.
* `get_share_price(symbol: str)`: Returns the current price of a share (this function is already provided).

#### Frontend Module (`app.py`)
The frontend module will use Gradio to create a user interface for the account management system. The Gradio app will have the following components:

* `create_account`: A function that creates a new account with a given initial balance.
* `deposit_funds`: A function that deposits a given amount into the account.
* `withdraw_funds`: A function that withdraws a given amount from the account.
* `buy_shares`: A function that buys a given quantity of shares of a given symbol.
* `sell_shares`: A function that sells a given quantity of shares of a given symbol.
* `get_holdings`: A function that returns the current holdings of the account.
* `get_portfolio_value`: A function that returns the current total value of the account's portfolio.
* `get_profit_loss`: A function that returns the current profit or loss of the account.
* `get_transaction_history`: A function that returns the transaction history of the account.

The Gradio app will use the following Gradio components:

* `gr.Interface`: To create the user interface.
* `gr.Number`: To input numbers (e.g. balance, amount, quantity).
* `gr.Textbox`: To input text (e.g. symbol).
* `gr.Dropdown`: To select from a list of options (e.g. buy/sell).
* `gr.Button`: To perform actions (e.g. create account, deposit funds).

The frontend engineer should use the latest Gradio 6 APIs, which have changes from earlier versions. Specifically, the `gr.Interface` component now requires a `fn` parameter, which is a function that takes the input values and returns the output values.

#### Unit Tests (`test_account_management.py`)
The test engineer will write unit tests for the backend module using the `unittest` framework. The tests will cover the following scenarios:

* Creating a new account with a given initial balance.
* Depositing funds into the account.
* Withdrawing funds from the account.
* Buying shares of a given symbol.
* Selling shares of a given symbol.
* Getting the current holdings of the account.
* Getting the current total value of the account's portfolio.
* Getting the current profit or loss of the account.
* Getting the transaction history of the account.

The test engineer should use the `unittest.TestCase` class to define test cases, and the `assert` statement to verify the expected behavior.

### Assignments

* `backend_engineer`: Write the backend Python code in `account_management.py`.
* `frontend_engineer`: Create the Gradio app in `app.py`.
* `test_engineer`: Write unit tests for the backend module in `test_account_management.py`.

### Notes

* The `get_share_price` function is already provided and will be used by the backend module to get the current price of a share.
* The Gradio app will use the latest Gradio 6 APIs, which have changes from earlier versions.
* The unit tests will cover the expected behavior of the backend module, including error cases (e.g. insufficient funds, invalid symbol).