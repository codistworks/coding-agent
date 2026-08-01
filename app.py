import gradio as gr
from account_management import Account, get_share_price

account = Account(0)

create_account = gr.Interface(
    fn=lambda balance: Account(balance),
    inputs=[gr.Number(label="Initial Balance")],
    outputs=["Account Created"],
    title="Create Account",
    description="Create a new account with an initial balance"
)

deposit_funds = gr.Interface(
    fn=lambda amount: account.deposit(amount),
    inputs=[gr.Number(label="Amount to Deposit")],
    outputs=["Funds Deposited"],
    title="Deposit Funds",
    description="Deposit funds into your account"
)

withdraw_funds = gr.Interface(
    fn=lambda amount: account.withdraw(amount),
    inputs=[gr.Number(label="Amount to Withdraw")],
    outputs=["Funds Withdrawn"],
    title="Withdraw Funds",
    description="Withdraw funds from your account"
)

buy_shares = gr.Interface(
    fn=lambda symbol, quantity: account.buy_shares(symbol, quantity),
    inputs=[gr.Textbox(label="Symbol"), gr.Number(label="Quantity")],
    outputs=["Shares Bought"],
    title="Buy Shares",
    description="Buy shares of a given symbol"
)

sell_shares = gr.Interface(
    fn=lambda symbol, quantity: account.sell_shares(symbol, quantity),
    inputs=[gr.Textbox(label="Symbol"), gr.Number(label="Quantity")],
    outputs=["Shares Sold"],
    title="Sell Shares",
    description="Sell shares of a given symbol"
)

get_holdings = gr.Interface(
    fn=lambda: account.get_holdings(),
    inputs=[],
    outputs=["Holdings"],
    title="Get Holdings",
    description="Get your current holdings"
)

get_portfolio_value = gr.Interface(
    fn=lambda: account.get_portfolio_value(),
    inputs=[],
    outputs=["Portfolio Value"],
    title="Get Portfolio Value",
    description="Get your current portfolio value"
)

get_profit_loss = gr.Interface(
    fn=lambda: account.get_profit_loss(),
    inputs=[],
    outputs=["Profit/Loss"],
    title="Get Profit/Loss",
    description="Get your current profit/loss"
)

get_transaction_history = gr.Interface(
    fn=lambda: account.get_transaction_history(),
    inputs=[],
    outputs=["Transaction History"],
    title="Get Transaction History",
    description="Get your transaction history"
)

block = gr.Blocks(
    [create_account, deposit_funds, withdraw_funds, buy_shares, sell_shares, get_holdings, get_portfolio_value, get_profit_loss, get_transaction_history]
)

if __name__ == "__main__":
    block.launch()