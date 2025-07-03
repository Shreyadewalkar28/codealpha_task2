stock_prices = {
    "APPLE": 120,
    "TESLA": 202,
    "GOOGLE": 120,
    "AMEZON": 1220,
}

total_investment = 0
n = int(input("Enter how many stocks you want to enter: "))

# ✅ Fixed the Unicode error with encoding="utf-8"
with open("portfolio_report.txt", "w", encoding="utf-8") as file:
    file.write("Stock Portfolio Report\n")
    file.write("-----------------------\n")

    for i in range(n):
        stock = input(f"Enter stock symbol #{i+1}: ").upper()
        quantity = int(input(f"Enter quantity of {stock}: "))

        if stock in stock_prices:
            price = stock_prices[stock]
            investment = price * quantity
            total_investment += investment

            print(f"{stock} x {quantity} @ ₹{price} = ₹{investment}")
            file.write(f"{stock} x {quantity} @ ₹{price} = ₹{investment}\n")
        else:
            print(f"Sorry, we don't have data for {stock}.")
            file.write(f"{stock} - Not found in price list\n")

    print(f"\nTotal Investment: ₹{total_investment}")
    file.write(f"\nTotal Investment: ₹{total_investment}\n")
