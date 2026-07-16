import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

# Number of different stocks
n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input(f"\nEnter stock name {i+1}: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock] = quantity
    else:
        print("Stock not found! Please choose from:", ", ".join(stock_prices.keys()))

print("\n------ Portfolio Summary ------")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock}")
    print(f"  Price per Share : ${price}")
    print(f"  Quantity        : {quantity}")
    print(f"  Investment      : ${investment}\n")

print(f"Total Investment Value = ${total_investment}")

# Save to TXT file
with open("portfolio.txt", "w") as txt_file:
    txt_file.write("STOCK PORTFOLIO REPORT\n")
    txt_file.write("-----------------------\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        txt_file.write(f"{stock} | Price: ${price} | Quantity: {quantity} | Investment: ${investment}\n")

    txt_file.write(f"\nTotal Investment = ${total_investment}")

# Save to CSV file
with open("portfolio.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(["Stock", "Price", "Quantity", "Investment"])

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        writer.writerow([stock, price, quantity, investment])

    writer.writerow([])
    writer.writerow(["Total Investment", "", "", total_investment])

print("\nPortfolio saved successfully in:")
print("1. portfolio.txt")
print("2. portfolio.csv")