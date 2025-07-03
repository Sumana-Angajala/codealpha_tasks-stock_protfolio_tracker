import csv
from datetime import datetime

# Hardcoded stock prices in USD
STOCK_PRICES_USD = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 125
}

# Currency conversion rates (approximate)
CURRENCY_RATES = {
    "USD": 1.0,
    "INR": 83.0  # You can update this rate as needed
}

def choose_currency():
    print("🌐 Choose your preferred currency:")
    for code in CURRENCY_RATES:
        print(f"- {code}")
    while True:
        choice = input("Enter currency code (USD/INR): ").upper()
        if choice in CURRENCY_RATES:
            return choice
        print("⚠️ Invalid choice. Please enter 'USD' or 'INR'.")

def prompt_portfolio():
    print("📊 Stock Portfolio Tracker")
    print("Available stocks:", ', '.join(STOCK_PRICES_USD.keys()))
    portfolio = {}
    total = 0

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES_USD:
            print("❗ Invalid stock. Please choose from the list.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
            if quantity < 0:
                raise ValueError
        except ValueError:
            print("⚠️ Enter a valid positive number.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        total += STOCK_PRICES_USD[stock] * quantity

    return portfolio, total

def display_summary(portfolio, total_usd, currency):
    rate = CURRENCY_RATES[currency]
    symbol = "₹" if currency == "INR" else "$"

    print(f"\n📋 Portfolio Summary ({currency}):")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES_USD[stock] * rate
        value = price * qty
        print(f"🔹 {stock}: {qty} x {symbol}{price:,.2f} = {symbol}{value:,.2f}")
    print(f"\n💼 Total Investment: {symbol}{total_usd * rate:,.2f}")

def save_to_files(portfolio, total_usd, currency):
    rate = CURRENCY_RATES[currency]
    symbol = "₹" if currency == "INR" else "$"
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_file = f"portfolio_summary_{currency}_{timestamp}.txt"
    csv_file = f"portfolio_summary_{currency}_{timestamp}.csv"

    with open(txt_file, "w") as txt:
        txt.write(f"Portfolio Summary ({currency}) - {now}\n\n")
        for stock, qty in portfolio.items():
            price = STOCK_PRICES_USD[stock] * rate
            value = price * qty
            txt.write(f"{stock}: {qty} x {symbol}{price:.2f} = {symbol}{value:.2f}\n")
        txt.write(f"\nTotal Investment: {symbol}{total_usd * rate:.2f}\n")

    with open(csv_file, "w", newline='') as csvout:
        writer = csv.writer(csvout)
        writer.writerow(["Stock", "Quantity", f"Price per Share ({currency})", f"Total Value ({currency})"])
        for stock, qty in portfolio.items():
            price = STOCK_PRICES_USD[stock] * rate
            writer.writerow([stock, qty, f"{symbol}{price:.2f}", f"{symbol}{price * qty:.2f}"])
        writer.writerow(["", "", "Total Investment", f"{symbol}{total_usd * rate:.2f}"])

    print(f"\n✅ Files saved:\n  • {txt_file}\n  • {csv_file}")

# 🟡 MAIN PROGRAM
currency = choose_currency()
portfolio, total_investment_usd = prompt_portfolio()
display_summary(portfolio, total_investment_usd, currency)

if input("\n📁 Save summary to .txt and .csv? (yes/no): ").lower() == "yes":
    save_to_files(portfolio, total_investment_usd, currency)