print("----Welcome to our Grocery store----")
print("Please choose a product from the provided list")
items = {
    "Milk": 1.99,
    "Eggs": 2.99,
    "Bread": 2.49,
    "Butter": 0.99,
    "Cheese": 3.49,
    "Apples": 1.49,
    "Bananas": 0.49,
    "Tomatoes": 2.29,
    "Potatoes": 1.99,
    "Onions": 1.29
}
print(items)
cart={}
while True:
    item_cart=input("Item:").capitalize().strip()
    quantity=int(input("Quantity:"))
    if item_cart not in items:
        while item_cart not in items:
            print("Please choose a product from the provided list")
            item_cart=input("Item:").capitalize().strip()
            quantity=int(input("Quantity:")) 
    else:
        cart[item_cart]=quantity
    cont=input("Type y to add more products and n to proceed to bill: ").lower().strip()
    if cont == 'y' or cont == 'yes':
        continue
    else:
        break
print("Items Quantity Price")
total=0
for k,v in cart.items():
    x=round(v*items[k],2)
    print(k," ",v," ",x)
    total+=x
print("your total is: ₹",total)
card=int(input("Enter your balance: "))
if total<card:
    print("Thank you for shopping with us; Your remaining balance is: ₹",card-total)
else:
    print("Oops you do not have sufficient balance please restart the program to order items within your balance")