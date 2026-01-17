menu = {
    'pasta': 50,
    'pizza': 60,
    'burger': 70,
    'coffee': 80,
}

print("Welcome to Arpan's Kitchen 🍽️")
print("Menu:")
print("pasta: Rs.50\npizza: Rs.60\nburger: Rs.70\ncoffee: Rs.80")

order_total = 0

while True:
    item = input("\nEnter the item you want to order (or type 'no' to finish): ").lower()

    if item == "no":
        break

    if item in menu:
        order_total += menu[item]
        print(f"{item} added to your order.")
    else:
        print("Sorry, this item is not available.")

print(f"\nYour total order amount is: Rs.{order_total}")
print("Thank you for dining with us! 🍽️")