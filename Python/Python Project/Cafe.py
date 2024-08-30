menu = {
    'Coffee' : 40,
    'Sprite' : 30,
    'Burger' : 50,
    'Pasta' : 60,
    'Pizza' : 70
}

print("\nWelcome to our CafeTeria\n")
print("Pizza  : Rs.70\nPasta  : Rs.60\nBurger : Rs.50\nCoffee : Rs.40\nSprite : Rs.30\n")
Total_Order = 0
Order = input("Enter the name of the food you want to order : ")
if Order in menu:
    Total_Order += menu[Order]
    print(f"Your Ordered item {Order} is Recived Successfully")
else:
    print(f"Ordered item {Order} is not available yet!")

Another_Order = input("Do you want to add another item in your order? (Yes/No) : ")
if Another_Order == 'Yes':
    Order2 = input("Enter the name of the second item : ")
    if Order2 in menu:
        Total_Order += menu[Order2]
        print(f"Item {Order2} has been added to order")
    else:
        print(f"Ordered item {Order} is not available yet!")

print(f"The total amount of items to pay is : {Total_Order}")