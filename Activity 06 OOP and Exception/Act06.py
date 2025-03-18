class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self):
        return f"Item(id={self.item_id}, name='{self.name}', description='{self.description}', price={self.price})"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        self.validate_item_id(item_id)
        self.validate_price(price)
        item = Item(item_id, name, description, price)
        self.items[item_id] = item
        print(f"Item created: {item}")
        return item

    def read_item(self, item_id):
        self.validate_item_id(item_id)
        return self.items.get(item_id, None)

    def update_item(self, item_id, name=None, description=None, price=None):
        self.validate_item_id(item_id)
        item = self.items.get(item_id)
        if not item:
            raise ValueError("Item not found")

        if name is not None:
            item.name = name
        if description is not None:
            item.description = description
        if price is not None:
            self.validate_price(price)
            item.price = price

        print(f"Item updated: {item}")
        return item

    def delete_item(self, item_id):
        self.validate_item_id(item_id)
        if item_id in self.items:
            del self.items[item_id]
            print(f"Item with ID {item_id} deleted.")
        else:
            raise ValueError("Item not found")

    def validate_item_id(self, item_id):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("Item ID must be a positive integer")

    def validate_price(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number")


if __name__ == "__main__":
    manager = ItemManager()

    while True:
        print("\nItem Management System")
        print("1. Create Item")
        print("2. Read Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List Items")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            try:
                item_id = int(input("Enter item ID: "))
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                item_id = int(input("Enter item ID to read: "))
                item = manager.read_item(item_id)
                print(item if item else "Item not found.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            try:
                item_id = int(input("Enter item ID to update: "))
                name = input("Enter new name (leave empty to skip): ")
                description = input("Enter new description (leave empty to skip): ")
                price_input = input("Enter new price (leave empty to skip): ")
                price = float(price_input) if price_input else None
                manager.update_item(item_id, name if name else None,
                                    description if description else None,
                                    price)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            try:
                item_id = int(input("Enter item ID to delete: "))
                manager.delete_item(item_id)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '5':
            print("Current items:")
            for item in manager.items.values():
                print(item)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")