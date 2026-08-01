```python
class Account:
    def __init__(self, balance: float):
        self.balance = balance
        self.holdings = {}
        self.transaction_history = []

    def deposit(self, amount: float):
        self.balance += amount
        self.transaction_history.append(f'Deposited {amount}')

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        self.transaction_history.append(f'Withdrew {amount}')

    def buy_shares(self, symbol: str, quantity: int):
        share_price = get_share_price(symbol)
        cost = share_price * quantity
        if cost > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        self.transaction_history.append(f'Bought {quantity} shares of {symbol}')

    def sell_shares(self, symbol: str, quantity: int):
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError('Insufficient shares')
        share_price = get_share_price(symbol)
        revenue = share_price * quantity
        self.balance += revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transaction_history.append(f'Sold {quantity} shares of {symbol}')

    def get_holdings(self):
        return self.holdings

    def get_portfolio_value(self):
        portfolio_value = self.balance
        for symbol, quantity in self.holdings.items():
            share_price = get_share_price(symbol)
            portfolio_value += share_price * quantity
        return portfolio_value

    def get_profit_loss(self):
        initial_balance = 0  # assuming initial balance is 0
        return self.get_portfolio_value() - initial_balance

    def get_transaction_history(self):
        return self.transaction_history


def get_share_price(symbol: str):
    # test implementation, replace with actual implementation
    if symbol == 'AAPL':
        return 100.0
    elif symbol == 'TSLA':
        return 500.0
    elif symbol == 'GOOGL':
        return 2000.0
    else:
        raise ValueError('Invalid symbol')
```