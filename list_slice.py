def main():
    cart = ["apple", "banana", "orange", "grape"]

    while True:
        view_cart = input("Do you want to view your cart? (yes/no): ").lower()

        if view_cart == "yes":
            print("Your cart contains:", cart)
            change_item = input("Do you want to change an item in your cart? (yes/no): ").lower()

            if change_item == "yes":
                item_to_change = input("Which item do you want to change? (apple, banana, orange, grape): ").lower()

                if item_to_change in cart:
                    new_fruit = input("Enter the new fruit for {}: ".format(item_to_change))
                    cart[cart.index(item_to_change)] = new_fruit
                    print("Your cart after change:", cart)
                else:
                    print("Invalid item! Please choose from apple, banana, orange, or grape.")

            else:
                break

        elif view_cart == "no":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid input! Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
