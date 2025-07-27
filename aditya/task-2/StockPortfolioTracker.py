# Step 1: Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3500,
    "MSFT": 310
}

# Step 2: Introduction
print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter 'done' when finished.\n")

portfolio = {}

# Step 3: User input loop
while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("❗ Quantity should be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid quantity. Must be a number.")

# Step 4: Calculate total investment
total_value = 0
print("\n📊 Your Stock Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity
    total_value += value
    print(f"{stock} - Qty: {quantity}, Price: ${price}, Value: ${value}")

print(f"\n💰 Total Investment Value: ${total_value}")

# Step 5: Optional - Save to file
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    filename = "portfolio_summary.txt"
    with open(filename, "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, quantity in portfolio.items():
            price = stock_prices[stock]
            value = price * quantity
            f.write(f"{stock}: Quantity={quantity}, Price=${price}, Value=${value}\n")
        f.write(f"\nTotal Investment Value: ${total_value}\n")
    print(f"✅ Portfolio saved to '{filename}'")
