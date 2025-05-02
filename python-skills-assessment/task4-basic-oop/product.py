#Product inventory app in python

inventory = {}

# define the product class

class Product:

    """
    ===Inventory systme app===

    Program working options:
    
        1. Add Product
        2. Remove Product
        3. Calculate Total
        4. Display Product
        5. Exit
    """

    def __init__(this, name, price, quantity=0):
        this.name = name
        this.price = price
        this.quantity = quantity

    #function to add product in inventory

    def add_product(this):
        product_id = len(inventory) + 1
        # Create a new dictionary for each product
        new_product = {
            'name': this.name,
            'price': this.price,
            'quantity': this.quantity
        }
        
        # Add the new product to inventory
        inventory[product_id] = new_product
        
        return inventory

    def remove_inventory(this, product_id):

        if product_id in inventory:
            del inventory[product_id]
        else:
            return "Product not found"
        

    def calculate_total(this, product_id):
        if product_id in inventory:
            product = inventory[product_id]

            return f"The total amount of product is: {product['price'] * product['quantity']}"
        else:
            return "Product selected not found"    
        
    def display_product(this, product_id):
        if product_id in inventory:
            product = inventory[product_id]

            return f"This is the full information about the product, Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}"
        
        else:
            return "Product selected not fount"
while True:
    print(Product.__doc__)
    print("")
    print("Current Inventory", inventory)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_name = input("Enter the name of your product: ")
        product_price = float(input("Product price: "))
        if product_price < 0:
            print("Product can not be negative!!")
            continue

        product_quantity = int(input("Product Quantity: "))

        if product_quantity < 0:
            print("Product quantity can not be negative")
            continue

        p = Product(product_name, product_price, product_quantity)
        p.add_product()

    elif choice == 2:
        product_id = int(input("Product id to remove"))
        res = p.remove_inventory(product_id)
        print(res if res else "Product remove")

    elif choice == 3:
        product_id = int(input("Product id to For calculating total: "))
        print(p.calculate_total(product_id))

    elif choice == 4:
        product_id = int(input("Product id to display: "))
        print(p.display_product(product_id))

    elif choice == 5:
        print("Closing the program")
        break

    else:
        print("Invalid choice try again")    