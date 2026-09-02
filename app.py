import gradio as gr
from account_management import Account, get_share_price

account = None

def create_account(initial_deposit):
    global account
    account = Account(initial_deposit)
    return "Account created"

def deposit_funds(amount):
    global account
    if account is not None:
        account.deposit(amount)
        return "Funds deposited"
    else:
        return "No account found"

def withdraw_funds(amount):
    global account
    if account is not None:
        try:
            account.withdraw(amount)
            return "Funds withdrawn"
        except ValueError as e:
            return str(e)
    else:
        return "No account found"

def buy_shares(symbol, quantity):
    global account
    if account is not None:
        try:
            account.buy_shares(symbol, quantity)
            return "Shares bought"
        except ValueError as e:
            return str(e)
    else:
        return "No account found"

def sell_shares(symbol, quantity):
    global account
    if account is not None:
        try:
            account.sell_shares(symbol, quantity)
            return "Shares sold"
        except ValueError as e:
            return str(e)
    else:
        return "No account found"

def get_account_holdings):
    global account
    if account is not None:
        return str(account.get_holdings())
    else:
        return "No account found"

def get_account_profit_loss):
    global account
    if account is not None:
        return str(account.get_profit_loss())
    else:
        return "No account found"

def get_account_transactions):
    global account
    if account is not None:
        return '\n'.join(account.get_transactions())
    else:
        return "No account found"

with gr.Blocks() as demo:
    gr.Markdown("# Account Management System")
    with gr.Tab("Account"):
        initial_deposit = gr.Number(label="Initial Deposit")
        create_account_button = gr.Button("Create Account")
        create_account_button.click(create_account, inputs=initial_deposit, outputs="result")
        gr.Textbox(label="Result")
    with gr.Tab("Transactions"):
        amount = gr.Number(label="Amount")
        deposit_button = gr.Button("Deposit")
        deposit_button.click(deposit_funds, inputs=amount, outputs="result")
        withdraw_button = gr.Button("Withdraw")
        withdraw_button.click(withdraw_funds, inputs=amount, outputs="result")
        gr.Textbox(label="Result")
    with gr.Tab("Shares"):
        symbol = gr.Textbox(label="Symbol")
        quantity = gr.Number(label="Quantity")
        buy_button = gr.Button("Buy")
        buy_button.click(buy_shares, inputs=[symbol, quantity], outputs="result")
        sell_button = gr.Button("Sell")
        sell_button.click(sell_shares, inputs=[symbol, quantity], outputs="result")
        gr.Textbox(label="Result")
    with gr.Tab("Account Info"):
        holdings_button = gr.Button("Get Holdings")
        holdings_button.click(get_account_holdings, outputs="result")
        gr.Textbox(label="Result")
        profit_loss_button = gr.Button("Get Profit/Loss")
        profit_loss_button.click(get_account_profit_loss, outputs="result")
        gr.Textbox(label="Result")
        transactions_button = gr.Button("Get Transactions")
        transactions_button.click(get_account_transactions, outputs="result")
        gr.Textbox(label="Result")

if __name__ == "__main__":
    demo.launch()



# comments here
