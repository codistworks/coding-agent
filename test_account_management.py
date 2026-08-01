import unittest
from account_management import Account, get_share_price

class TestAccountManagement(unittest.TestCase):
    def test_account_creation(self):
        account = Account(1000)
        self.assertEqual(account.initial_deposit, 1000)
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.holdings, {})
        self.assertEqual(account.transaction_history, [])

    def test_deposit(self):
        account = Account(1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)
        self.assertEqual(account.transaction_history, ['Deposited 500'])

    def test_withdraw(self):
        account = Account(1000)
        account.withdraw(500)
        self.assertEqual(account.balance, 500)
        self.assertEqual(account.transaction_history, ['Withdrew 500'])

    def test_buy_shares(self):
        account = Account(1000)
        account.buy_shares('AAPL', 5)
        self.assertEqual(account.holdings, {'AAPL': 5})
        self.assertEqual(account.balance, 900)
        self.assertEqual(account.transaction_history, ['Bought 5 AAPL shares'])

    def test_sell_shares(self):
        account = Account(1000)
        account.buy_shares('AAPL', 5)
        account.sell_shares('AAPL', 3)
        self.assertEqual(account.holdings, {'AAPL': 2})
        self.assertEqual(account.balance, 950)
        self.assertEqual(account.transaction_history, ['Bought 5 AAPL shares', 'Sold 3 AAPL shares'])

    def test_get_portfolio_value(self):
        account = Account(1000)
        account.buy_shares('AAPL', 5)
        self.assertEqual(account.get_portfolio_value(), 1900)

    def test_get_profit_loss(self):
        account = Account(1000)
        account.buy_shares('AAPL', 5)
        self.assertEqual(account.get_profit_loss(), 900)

    def test_get_holdings(self):
        account = Account(1000)
        account.buy_shares('AAPL', 5)
        self.assertEqual(account.get_holdings(), {'AAPL': 5})

    def test_get_transaction_history(self):
        account = Account(1000)
        account.deposit(500)
        account.buy_shares('AAPL', 5)
        self.assertEqual(account.get_transaction_history(), ['Deposited 500', 'Bought 5 AAPL shares'])

if __name__ == '__main__':
    unittest.main()