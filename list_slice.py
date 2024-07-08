cart = ['Strawberrys', 'Bananas', 'Apple']
User_ask1 = input("Do you want to view your Cart?: ")
if User_ask1 == 'Yes' or 'yes':
    print(cart)
Userask2 = input("Do you want to change items in your cart?: ")
User_ask3 = input("which item do you want to change from the cart: ")
if User_ask3 == 'Strawberry' or 'strawberry':
    Userask4 = input("Change to: ")
cart[0] = Userask4
print(cart)