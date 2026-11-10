class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    @staticmethod
    def is_valid_price(price):
        return price > 0

    @staticmethod
    def is_valid_stock(quantity):
        return quantity >= 0

    @classmethod
    def create_validated(cls, product_id, name, price, stock_quantity):
        if not product_id.strip():
            print("Product ID cannot be empty.")
            return None

        if not name.strip():
            print("Product name cannot be empty.")
            return None

        if not cls.is_valid_price(price):
            print("Product price must be greater than zero.")
            return None

        if not cls.is_valid_stock(stock_quantity):
            print("Stock quantity cannot be negative.")
            return None

        return cls(product_id.strip(), name.strip(), price, stock_quantity)

class InventoryManager:
    def __init__(self):
        self.products = {}

    @staticmethod
    def is_positive_quantity(quantity):
        return quantity > 0

    def add_product(self):
        product_id = input("\nEnter Product ID : ").strip()

        if product_id in self.products :
            print(f"The product with product id '{product_id}' already exists.")
            return

        name = input("Enter Product's name : ").strip()


        try:
            price = float(input("Enter Product's Price : Rs. "))
            stock_quantity = int(input("Enter Product's Stock Quantity : "))
        except ValueError:
            print("\nPlease enter valid numeric values.")
            return


        product = Product.create_validated(product_id, name, price, stock_quantity)

        if product is not None:
            self.products[product_id] = product
            print("Product added successfully!")

    def display_products(self):
        if len(self.products) == 0:
            print("No products available.")
            return

        print("\n========== PRODUCT DETAILS ==========")
        
        for product in self.products.values():
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.name}")
            print(f"Product Price: Rs. {product.price}")
            print(f"Stock Quantity: {product.stock_quantity}")
            print("--------------------------------")

    def search_product(self, product_id):
        if product_id in self.products:
            product = self.products[product_id]

            print(f"Product Id: {product.product_id}\nProduct Name: {product.name}\nProduct Price: {product.price}\nStock Quantity: {product.stock_quantity}")
        else:
            print("Product Not Found !")

    def update_stock(self, product_id, quantity):
        if product_id in self.products:
            product = self.products[product_id]


            if not self.is_positive_quantity(quantity):
                print("Quantity must be greater than zero.")
                return

            product.stock_quantity += quantity

            print("\nStock Updated Successfully!")
            print(f"Product ID: {product.product_id}")
            print(f"Product Name: {product.name}")
            print(f"Product Price: Rs. {product.price:.2f}")
            print(f"Stock Quantity: {product.stock_quantity}")

        else:
            print("Product Not Found!")

    def sell_product(self, product_id, quantity):
        if product_id in self.products:
            product = self.products[product_id]

            if not self.is_positive_quantity(quantity):
                print("Quantity must be greater than zero.")
                return

            elif product.stock_quantity < 0:
                print("Invalid stock quantity.")
                return

            elif product.stock_quantity == 0:
                print(f"{product.name} is out of stock!")
                return

            elif quantity > product.stock_quantity:
                    print(f"Insufficient Stock!\nAvailable Stock: {product.stock_quantity}")
                    
                    all_purchase = input(f"Would you like to purchase all {product.stock_quantity} available items? (Y/N):").upper()

                    while(all_purchase not in ('Y', 'N')):
                        print("You can only enter 'Y' for Yes or 'N' for No.")
                        all_purchase = input("Enter your choice (Y/N): ").upper()
                    
                    if(all_purchase == 'Y'):
                        purchase_quantity = product.stock_quantity
                    elif(all_purchase == 'N'):
                        print("Purchase Cancelled")
                        return
            else:
                purchase_quantity = quantity

            product.stock_quantity -= purchase_quantity

            bill = product.price * purchase_quantity
            
            print(f"Purchase Successful!\nProduct Id: {product.product_id}\nProduct Name: {product.name}\nPurchased Quantity: {purchase_quantity}\nRemaining Stock: {product.stock_quantity}\nTotal Bill: {bill}")
        else:
            print("Product Not Found !")


    def calculate_inventory_values(self):

        if len(self.products) == 0:
            print("Inventory is empty.")
            return

        print("Product\tPrice\tStock\tValue")

        total_value = 0

        for product in self.products.values():
            product_value = product.price * product.stock_quantity

            total_value += product_value 

            print(f"{product.name}\t{product.price}\t{product.stock_quantity}\t{product_value}")

        print("------------------------------------------")
        print(f"Total Inventory Value : Rs. {total_value}")

    def calculate_total_unit(self):
        total_units = 0

        if len(self.products) == 0:
            print("Inventory is empty.")
            return

        for product in self.products.values():
            total_units += product.stock_quantity

        if total_units != 0:
            print(f"Total Unit : {total_units}")
        else:
            print("No units available in the inventory")

    def display_low_stock(self):
        threshold = 5
        low_stock_found = False
        
        if(len(self.products) == 0):
                print("Inventory is empty.")
                return
        
        for product in self.products.values():
            if product.stock_quantity < threshold:
                low_stock_found = True
                print(f"Product Id: {product.product_id}\nProduct Name: {product.name}\nRemaining Stock: {product.stock_quantity}")
        if low_stock_found == False:
            print("No low-stock products found.")            

def main():
        inventory = InventoryManager()

        while True:
            print("\n========== INVENTORY MANAGEMENT SYSTEM ==========")
            print("1. Add Product")
            print("2. Display Products")
            print("3. Search Product")
            print("4. Update Stock")
            print("5. Sell Product")
            print("6. Calculate Inventory Value")
            print("7. Calculate Total Units")
            print("8. Display Low Stock")
            print("9. Exit")

            try:
                choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Please enter a valid numeric choice.")
                continue

            if choice == 1:
                inventory.add_product()
            elif choice == 2:
                inventory.display_products()
            elif choice == 3:
                product_id = input("Enter Product ID: ").strip()
                inventory.search_product(product_id)
            elif choice == 4:
                product_id = input("Enter Product ID: ").strip()

                try:
                    quantity = int(input("Enter quantity to add: "))
                except ValueError:
                    print("Please enter a valid integer quantity.")
                    continue

                inventory.update_stock(product_id,quantity)

            elif choice == 5:
                product_id = input("Enter Product ID: ").strip()

                try:
                    quantity = int(input("Enter quantity to purchase: "))
                except ValueError:
                    print("Please enter a valid integer quantity.")
                    continue

                inventory.sell_product(product_id,quantity)

            elif choice == 6:
                inventory.calculate_inventory_values()
            elif choice == 7:
                inventory.calculate_total_unit()
            elif choice == 8:
                inventory.display_low_stock()
            elif choice == 9:
                print("\nThank you for using the Inventory Management System!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 9.")


if __name__ == "__main__":
    main()