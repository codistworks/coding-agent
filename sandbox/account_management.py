```python
import datetime

class Transaction:
    def __init__(self, user_id, timestamp, type, symbol, quantity, price, total_cost):
        self.user_id = user_id
        self.timestamp = timestamp
        self.type = type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.total_cost = total_cost

class Account:
    def __init__(self, user_id, initial_deposit):
        self.user_id = user_id
        self.balance = initial_deposit
        self.holdings = {}
        self.transactions = []
        self.initial_deposit = initial_deposit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise ValueError("Insufficient funds for withdrawal.")
        self.balance -= amount

    def buy_share(self, symbol, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        price = get_share_price(symbol)
        total_cost = price * quantity
        if self.balance < total_cost:
            raise ValueError(f"Insufficient funds to buy {quantity} shares of {symbol}.")
        self.balance -= total_cost
        if symbol in self.holdings:
            self.holdings[symbol] += quantity
        else:
            self.holdings[symbol] = quantity
        transaction = Transaction(
            self.user_id,
            datetime.datetime.now(),
            'buy',
            symbol,
            quantity,
            price,
            total_cost
        )
        self.transactions.append(transaction)

    def sell_share(self, symbol, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if symbol not in self.holdings or self.holdings[symbol] < quantity:
            raise ValueError(f"Insufficient holdings of {symbol} to sell {quantity} shares.")
        price = get_share_price(symbol)
        total_revenue = price * quantity
        self.balance += total_revenue
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        transaction = Transaction(
            self.user_id,
            datetime.datetime.now(),
            'sell',
            symbol,
            quantity,
            price,
            total_revenue
        )
        self.transactions.append(transaction)

    def get_holdings(self):
        return self.holdings.copy()

    def get_transactions(self):
        return self.transactions.copy()

    def get_portfolio_value(self):
        portfolio_value = self.balance
        for symbol, qty in self.holdings.items():
            portfolio_value += qty * get_share_price(symbol)
        return portfolio_value

    def get_profit_loss(self):
        return self.get_portfolio_value() - self.initial_deposit

    def get_balance(self):
        return self.balance

def get_share_price(symbol):
    prices = {
        'AAPL': 150.0,
        'TSLA': 250.0,
        'GOOGL': 280.0
    }
    return prices.get(symbol, 0.0)
```