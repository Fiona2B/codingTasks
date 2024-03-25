# This programme will create a menu for a cafe.
# There will be a dictionary for the stock value of the items.
# And a dictionary for the prices of the items on the menu.
# Then it will calculate the total stock worth in the cafe and print the results.

# Cafe Menu.
menu = [
        "coffee",
        "tea",
        "juice",
        "cake",
        "cookie"
        ]
# Stock count for each item.
stock = {
        "coffee" : 150,
        "tea" : 500,
        "juice" : 100,
        "cake" : 20,
        "cookie" : 50,
        }
# Menu prices.
prices = {"coffee" : 2.00,
          "tea" : 1.75,
          "juice" : 1.50,
          "cake" : 3.00,
          "cookie" : 2.50,
            }

# Calculates total stock worth in cafe.
total_stock_value = 0
for key in stock:
    if key in prices:
        total_stock_value += stock[key] * prices[key]
print(f"Total stock value in cafe: " + str(total_stock_value))
