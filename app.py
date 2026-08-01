import gradio as gr
from account_management import Account

account = Account(1000)

def create_account(initial_deposit):
    account = Account(initial_deposit)
    return account

def deposit_funds(amount):
    account.deposit(amount)
    return account.balance

def withdraw_funds(amount):
    account.withdraw(amount)
    return account.balance

def buy_shares(symbol, quantity):
    account.buy_shares(symbol, quantity)
    return account.holdings

def sell_shares(symbol, quantity):
    account.sell_shares(symbol, quantity)
    return account.holdings

def get_portfolio_value):
    return account.get_portfolio_value()

def get_profit_loss):
    return account.get_profit_loss()

def get_holdings):
    return account.get_holdings()

def get_transaction_history):
    return account.get_transaction_history()

interface = gr.Interface(
    fn=lambda initial_deposit, amount, symbol, quantity: (
        create_account(initial_deposit),
        deposit_funds(amount),
        withdraw_funds(amount),
        buy_shares(symbol, quantity),
        sell_shares(symbol, quantity),
        get_portfolio_value(),
        get_profit_loss(),
        get_holdings(),
        get_transaction_history()
    ),
    inputs=[
        gr.Textbox(label="Initial Deposit"),
        gr.Textbox(label="Amount to Deposit"),
        gr.Textbox(label="Symbol"),
        gr.Textbox(label="Quantity to Buy/Sell")
    ],
    outputs=[
        gr.Textbox(label="Account"),
        gr.Textbox(label="Balance"),
        gr.Textbox(label="Holdings"),
        gr.Textbox(label="Portfolio Value"),
        gr.Textbox(label="Profit/Loss"),
        gr.Textbox(label="Transaction History")
    ],
    title="Account Management System"
)
interface.launch()