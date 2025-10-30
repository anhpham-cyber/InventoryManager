def add_product(inventory: dict) -> None:
    while True:
        name = input("Please enter a name of a product: ").title()
        if not name:
            print("Cannot leave product's name empty!")
        else:
            break
    
    while True:
        price = input("Enter the price of a product: $")

        if not price:
            print("Price cannot be empty!")
            continue

        try:
            price = float(price)
            if price < 0:
                print("Price cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
        
    while True:
        quantity = input("Please enter quantity for this product: ")
        if not quantity:
            print("Cannot leave product's quantity empty!")
        elif not quantity.isdigit():
            print("Product's quantity must be a whole positive number!")
        else:
            quantity = int(quantity)
            break
    
    inventory[name] = {"price": price, "quantity": quantity}
    print(f"{name} has been added to the inventory at ${price:.2f} with a quantity of {quantity}.")


def view_product(inventory):
    if not inventory:
        print("The inventory is empty.")
        return
    
    print("\nInventory List")
    print("---------------------------------")
    for name, details in inventory.items():
        print(f"Product: {name}")
        print(f"   Price: ${details['price']:.2f}")
        print(f"   Quantity: {details['quantity']}")
        print("---------------------------------")

def update_information(inventory):
    if not inventory:
        print("The inventory is empty. No information to update!")
        return
    
    while True:
        print("\n-----UPDATE-----")
        print("1. Product's name")
        print("2. Product's price")
        print("3. Product's quantity")
        print("4. Exit")

        update = input("What information do you want to update today (1-4): ")
        
        if update == "1":

            old_name = input("Please enter a current name of the product: ").title()
            if old_name not in inventory:
                print(f"There is no '{old_name}' in the inventory!")
                return
            while True:
                new_name = input("Please enter a new name of this product: ").title()
                if not new_name:
                    print("Cannot leave product's name empty!")
                else:
                    break
            inventory[new_name] = inventory.pop(old_name)
            print(f"{new_name} has been updated to the inventory!")
            break

        elif update == "2":
            
            name = input("Please enter product's name: ").title()
            if name not in inventory:
                print(f"There is no '{name}' in the inventory!")
                return
            while True:
                new_price = input("Please enter your new price: $")
                
                if not new_price:
                    print("Cannot leave product's price empty!")
                    continue
                
                try:
                    new_price = float(new_price)
                    inventory[name]["price"] = new_price
                    if new_price < 0:
                        print("Price cannot be negative!")
                        continue
                    break
                except ValueError:
                    print("Invalid input! Please enter a number.")
                break
            print(f"New price for '{name}' has been updated!")
            break
                      
        elif update == "3":
            
            name = input("Please enter product's name: ").title()
            if name not in inventory:
                print(f"There is no '{name}' in the inventory!")
                return
            while True:
                new_quantity = input("Please enter your new quantity: ")
                if not new_quantity.isdigit():
                    print("Invalid, quantity must be a positive number!")
                    continue

                if not new_quantity:
                    print("Cannot leave product's quantity empty!")
                    continue
                
                new_quantity = int(new_quantity)
                inventory[name]["quantity"] = new_quantity
                break
            print(f"New quantity for '{name}' has been updated!")
            break

        elif update == "4":
            break

        else:
            print(f"{update} is an invalid input, please select an option between 1-4!")

def process_sales(inventory, revenue):
    if not inventory:
        print("The inventory is empty. No information to process sales!")
        return

    while True:
        name = input("Please enter name of the selling product: ").title()
        if not name:
            print("Cannot leave product's name empty!")
        elif name not in inventory:
            print(f"'{name}' is not in the inventory")
        else:
            break
        
    while True:
        sell_qty = input("Please enter the quantity of a selling product: ")
        if not sell_qty:
            print("Cannot leave product's quantity empty!")
        elif not sell_qty.isdigit():
            print("Product's quantity must be a positive number!")
        else:
            sell_qty = int(sell_qty)
            break

   
    price = inventory[name]["price"]
    

    if sell_qty <= inventory[name]["quantity"]:
        total_sales = price * sell_qty
        revenue.append(total_sales)
        inventory[name]["quantity"] -= sell_qty
        print(f"Sold {sell_qty} '{name}' for ${total_sales:.2f}")
        print(f"Remaining '{name}' quantity: {inventory[name]['quantity']}")
    else:
        print(f"Insufficent quantity of '{name}'")
        print(f"'{name}' quantity: {inventory[name]['quantity']}")


def total_rev(revenue):
    total_revenue = 0

    for i, transaction in enumerate(revenue, start=1):
        print(f"Transaction {i}: ${transaction:.2f}")
        total_revenue += transaction
    print(f"Today total revenue is ${total_revenue:.2f}")

def search_product(inventory):
    if not inventory:
        print("Inventory is empty!")
        return
    name = input("Please enter product name to search: ").title()
    if name not in inventory:
        print(f"'{name}' is not in the inventory")
    else:
        print(f"Product: {name}, Price: {inventory[name]['price']:.2f}, Quantity: {inventory[name]['quantity']}")

def main():
    print("---------------------------")
    print("Inventory Management System")
    print("---------------------------")

    inventory = {}
    revenue = []
    while True:
        
        print("\n-----------------   Menu   -----------------")
        print("1. Add new product to the inventory")
        print("2. View all products with detail")
        print("3. Update product information (restock)")
        print("4. Process sales: \n(sell products, reduce stock, calculate total sale)")
        print("5. Track total revenue for the day")
        print("6. Search products by name")
        print("7. Exit")
        print("--------------------------------------------")

        select = input("Please select an option (1-7): ")

        if select == "1":
            add_product(inventory)
        elif select == "2":
            view_product(inventory)
        elif select == "3":
            update_information(inventory)
        elif select == "4":
            process_sales(inventory, revenue)
        elif select == "5":
            total_rev(revenue)
        elif select == "6":
            search_product(inventory)
        elif select == "7":
            print("\n---------------------------------------------------------")
            print("Thank you for using Inventory Management System. Goodbye!")
            print("---------------------------------------------------------")
            break
        else:
            print(f"{select} is an invalid input. Please select an option between 1-7!")


if __name__ == "__main__":
    main()