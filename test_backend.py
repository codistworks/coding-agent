import unittest
from unittest.mock import patch

class TestAccountManagement(unittest.TestCase):
    def test_create_account(self):
        account = Account(1000)
        self.assertEqual(account.initial_deposit, 1000)
        self.assertEqual(account.balance, 1000)
        self.assertEqual(account.holdings, {})
        self.assertEqual(account.transactions, [])

    def test_deposit(self):
        account = Account(1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)
        self.assertEqual(account.transactions, ['Deposited 500'])

    def test_withdraw(self):
        account = Account(1000)
        account.withdraw(200)
        self.assertEqual(account.balance, 800)
        self.assertEqual(account.transactions, ['Withdrew 200'])

    def test_buy_shares(self):
        account = Account(1000)
        with patch('get_share_price') as mock_get_share_price:
            mock_get_share_price.return_value = 100.0
            account.buy_shares('AAPL', 10)
            self.assertEqual(account.balance, 900)
            self.assertEqual(account.holdings, {'AAPL': 10})
            self.assertEqual(account.transactions, ['Bought 10 AAPL shares'])

    def test_sell_shares(self):
        account = Account(1000)
        account.holdings = {'AAPL': 10}
        with patch('get_share_price') as mock_get_share_price:
            mock_get_share_price.return_value = 100.0
            account.sell_shares('AAPL', 5)
            self.assertEqual(account.balance, 1050)
            self.assertEqual(account.holdings, {'AAPL': 5})
            self.assertEqual(account.transactions, ['Sold 5 AAPL shares'])

    def test_get_holdings(self):
        account = Account(1000)
        account.holdings = {'AAPL': 10, 'TSLA': 5}
        self.assertEqual(account.get_holdings(), {'AAPL': 10, 'TSLA': 5})

    def test_get_profit_loss(self):
        account = Account(1000)
        account.balance = 1200
        self.assertEqual(account.get_profit_loss(), 200)

    def test_get_transactions(self):
        account = Account(1000)
        account.transactions = ['Deposited 500', 'Withdrew 200', 'Bought 10 AAPL shares']
        self.assertEqual(account.get_transactions(), ['Deposited 500', 'Withdrew 200', 'Bought 10 AAPL shares'])

if __name__ == '__main__':
    class Account:
        def __init__(self, initial_deposit):
            self.initial_deposit = initial_deposit
            self.balance = initial_deposit
            self.holdings = {}
            self.transactions = []

        def deposit(self, amount):
            self.balance += amount
            self.transactions.append(f'Deposited {amount}')

        def withdraw(self, amount):
            if amount > self.balance:
                raise ValueError('Insufficient balance')
            self.balance -= amount
            self.transactions.append(f'Withdrew {amount}')

        def buy_shares(self, symbol, quantity):
            price = get_share_price(symbol)
            cost = price * quantity
            if cost > self.balance:
                raise ValueError('Insufficient balance')
            self.balance -= cost
            if symbol in self.holdings:
                self.holdings[symbol] += quantity
            else:
                self.holdings[symbol] = quantity
            self.transactions.append(f'Bought {quantity} {symbol} shares')

        def sell_shares(self, symbol, quantity):
            if symbol not in self.holdings or self.holdings[symbol] < quantity:
                raise ValueError('Insufficient shares')
            price = get_share_price(symbol)
            revenue = price * quantity
            self.balance += revenue
            self.holdings[symbol] -= quantity
            if self.holdings[symbol] == 0:
                del self.holdings[symbol]
            self.transactions.append(f'Sold {quantity} {symbol} shares')

        def get_holdings(self):
            return self.holdings

        def get_profit_loss(self):
            return self.balance - self.initial_deposit

        def get_transactions(self):
            return self.transactions

    def get_share_price(symbol):
        prices = {
            'AAPL': 100.0,
            'TSLA': 500.0,
            'GOOGL': 2000.0
        }
        return prices.get(symbol, 0.0)

    unittest.main()