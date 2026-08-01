def get_share_price(symbol):
    # Test implementation, replace with actual implementation
    if symbol == 'AAPL':
        return 100.0
    elif symbol == 'TSLA':
        return 500.0
    elif symbol == 'GOOGL':
        return 2000.0
    else:
        raise ValueError('Unknown symbol')

class Account:
    def __init__(self, initial_deposit):
        self.initial_deposit = initial_deposit
        self.balance = initial_deposit
        self.holdings = {}
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f'Deposited {amount}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        self.transaction_history.append(f'Withdrew {amount}')

    def buy_shares(self, symbol, quantity):
        share_price = get_share_price(symbol)
        cost = share_price * quantity
        if cost > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transaction_history.append(f'Bought {quantity} {symbol} shares')

    def sell_shares(self, symbol, quantity):
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError('Insufficient shares')
        share_price = get_share_price(symbol)
        revenue = share_price * quantity
        self.balance += revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transaction_history.append(f'Sold {quantity} {symbol} shares')

    def get_portfolio_value(self):
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            portfolio_value += get_share_price(symbol) * quantity
        return portfolio_value

    def get_profit_loss(self):
        return self.get_portfolio_value() - self.initial_deposit

    def get_holdings(self):
        return self.holdings

    def get_transaction_history(self):
        return self.transaction_history

import unittest

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