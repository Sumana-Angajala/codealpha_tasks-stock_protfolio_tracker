# codealpha_tasks-stock_protfolio_tracker
Here's a **GitHub README-style description** for your **Stock Portfolio Tracker** Python script:

---

## 📊 Stock Portfolio Tracker (Command-Line App)

A simple, interactive **command-line tool** that helps you track your stock investments. It supports **USD and INR currencies**, displays a portfolio summary, and exports your results to **TXT and CSV** files.

---

### 🚀 Features

* 🔍 Choose between **USD** or **INR** as your preferred currency.
* 📈 Track investments in major tech stocks: AAPL, TSLA, GOOGL, MSFT, and AMZN.
* ✅ Input stock quantities and get a real-time investment summary.
* 💰 Calculates the **total investment value** based on hardcoded prices.
* 📤 Option to export the portfolio summary to:

  * `.txt` (human-readable summary)
  * `.csv` (tabular format for spreadsheets)

---

### 📦 Supported Stocks and Prices (in USD)

| Symbol | Company   | Price (USD) |
| ------ | --------- | ----------- |
| AAPL   | Apple     | \$180       |
| TSLA   | Tesla     | \$250       |
| GOOGL  | Alphabet  | \$135       |
| MSFT   | Microsoft | \$320       |
| AMZN   | Amazon    | \$125       |

---

### 🌍 Supported Currencies

| Code | Name         | Rate (approx.) |
| ---- | ------------ | -------------- |
| USD  | US Dollar    | 1.00           |
| INR  | Indian Rupee | 83.00          |

---

### 🛠 Requirements

* Python 3.x
* No external libraries required

---

### 🧑‍💻 How to Use

1. **Run the script**:

```bash
python stock_portfolio_tracker.py
```

2. **Choose currency**: USD or INR
3. **Enter stock symbols and quantities** (type `done` to finish)
4. **View the investment summary**
5. **Optional**: Save your portfolio to `.txt` and `.csv` files

---

### 📁 Example Output

```
🌐 Choose your preferred currency:
- USD
- INR
Enter currency code (USD/INR): INR

📊 Stock Portfolio Tracker
Available stocks: AAPL, TSLA, GOOGL, MSFT, AMZN
Enter stock symbol (or 'done' to finish): AAPL
Enter quantity of AAPL: 5
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity of TSLA: 2
Enter stock symbol (or 'done' to finish): done

📋 Portfolio Summary (INR):
🔹 AAPL: 5 x ₹14,940.00 = ₹74,700.00
🔹 TSLA: 2 x ₹20,750.00 = ₹41,500.00

💼 Total Investment: ₹116,200.00

📁 Save summary to .txt and .csv? (yes/no): yes

✅ Files saved:
  • portfolio_summary_INR_20250703_143211.txt
  • portfolio_summary_INR_20250703_143211.csv
```

---

### 📌 Notes

* You can update stock prices and currency rates directly in the `STOCK_PRICES_USD` and `CURRENCY_RATES` dictionaries.
* Great for practicing beginner Python skills such as:

  * Input/output
  * Dictionaries
  * File handling
  * Basic error checking

---

