from sweetshop.inventory import Inventory
from sweetshop.models import Sweet

def display_menu():
    """Display the main menu options with emojis"""
    print("-" * 65)
    print("\n🍬 Sweet Shop Management System 🍭")
    print("-" * 65)
    print("1. 🆕 Add Sweet")
    print("2. ❌ Delete Sweet")
    print("3. 👀 View All Sweets")
    print("4. 🔍 Search Sweets")
    print("5. 🔄 Sort Sweets")
    print("6. 🛒 Purchase Sweet")
    print("7. 📦 Restock Sweet")
    print("0. 🚪 Exit")

def get_integer_input(prompt, min_val=None, max_val=None):
    """Get validated integer input from user"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"⚠️ Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"⚠️ Value must be at most {max_val}")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid integer.")

def get_float_input(prompt, min_val=None):
    """Get validated float input from user"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"⚠️ Value must be at least {min_val}")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")

def get_string_input(prompt, min_length=1):
    """Get validated string input from user"""
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        print(f"⚠️ Input must be at least {min_length} character(s) long.")

def add_sweet_cli(inventory):
    """Handle adding a new sweet via CLI"""
    print("\n➕ Add New Sweet")
    try:
        sweet_id = get_integer_input("Enter sweet ID: ", min_val=1)
        name = get_string_input("Enter sweet name: ")
        category = get_string_input("Enter category: ")
        price = get_float_input("Enter price: ", min_val=0.01)
        quantity = get_integer_input("Enter initial quantity: ", min_val=0)
        
        sweet = Sweet(id=sweet_id, name=name, category=category, 
                     price=price, quantity=quantity)
        inventory.add_sweet(sweet)
        print(f"✅ Successfully added {name} to inventory!")
    except ValueError as e:
        print(f"❌ Error: {e}")

def delete_sweet_cli(inventory):
    """Handle deleting a sweet via CLI"""
    print("\n🗑️ Delete Sweet")
    if not inventory.sweets:
        print("📭 Inventory is empty.")
        return
    
    sweet_id = get_integer_input("Enter sweet ID to delete: ", min_val=1)
    try:
        inventory.delete_sweet(sweet_id)
        print("✅ Sweet deleted successfully!")
    except KeyError:
        print("❌ Error: Sweet not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def view_all_sweets_cli(inventory):
    """Display all sweets in inventory"""
    print("\n👀 All Sweets in Inventory\n")
    sweets = inventory.view_all_sweets()
    if not sweets:
        print("📭 Inventory is empty.")
        return
    print("-" * 65)
    print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10} {'Quantity':<10}")
    print("-" * 65)
    for sweet in sweets:
        print(f"{sweet.id:<5} {sweet.name:<20} {sweet.category:<15} "
              f"${sweet.price:<9.2f} {sweet.quantity:<10}")

def search_sweets_cli(inventory):
    """Handle searching sweets via CLI"""
    print("\n🔍 Search Sweets")
    print("Leave any field blank to skip that filter")
    
    name = input("Enter name (or partial name) to search: ").strip() or None
    category = input("Enter category to search: ").strip() or None
    
    min_price = None
    max_price = None
    try:
        min_price_input = input("Enter minimum price (leave blank for none): ").strip()
        if min_price_input:
            min_price = float(min_price_input)
        
        max_price_input = input("Enter maximum price (leave blank for none): ").strip()
        if max_price_input:
            max_price = float(max_price_input)
    except ValueError:
        print("⚠️ Invalid price input. Using no price filters.")
        min_price = max_price = None
    
    try:
        results = inventory.search_sweets(
            name=name,
            category=category,
            min_price=min_price,
            max_price=max_price
        )
        
        print(f"\n🔎 Found {len(results)} matching sweet(s):\n")
        if results:
            print("-" * 65)
            print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10} {'Quantity':<10}")
            print("-" * 65)
            for sweet in results:
                print(f"{sweet.id:<5} {sweet.name:<20} {sweet.category:<15} "
                      f"${sweet.price:<9.2f} {sweet.quantity:<10}")
        else:
            print("😞 No sweets match your search criteria.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def sort_sweets_cli(inventory):
    """Handle sorting sweets via CLI"""
    print("\n🔄 Sort Sweets")
    if not inventory.sweets:
        print("📭 Inventory is empty.")
        return
    
    print("Sort by:")
    print("1. Name")
    print("2. Category")
    print("3. Price")
    choice = get_integer_input("Enter your choice (1-3): ", min_val=1, max_val=3)
    
    order = input("Sort order (A)scending or D)escending? [A/D]: ").strip().upper()
    reverse = order == 'D'
    
    sort_keys = {1: "name", 2: "category", 3: "price"}
    try:
        sorted_sweets = inventory.sort_sweets(key=sort_keys[choice], reverse=reverse)
        
        print("\n📊 Sorted Results:\n")
        print("-" * 65)
        print(f"{'ID':<5} {'Name':<20} {'Category':<15} {'Price':<10} {'Quantity':<10}")
        print("-" * 65)
        for sweet in sorted_sweets:
            print(f"{sweet.id:<5} {sweet.name:<20} {sweet.category:<15} "
                  f"${sweet.price:<9.2f} {sweet.quantity:<10}")
    except ValueError as e:
        print(f"❌ Error: {e}")

def purchase_sweet_cli(inventory):
    """Handle purchasing sweets via CLI"""
    print("\n🛒 Purchase Sweet")
    if not inventory.sweets:
        print("📭 Inventory is empty.")
        return
    
    sweet_id = get_integer_input("Enter sweet ID to purchase: ", min_val=1)
    quantity = get_integer_input("Enter quantity to purchase: ", min_val=1)
    
    try:
        inventory.purchase_sweet(sweet_id, quantity)
        print(f"✅ Successfully purchased {quantity} item(s)! 🎉")
    except KeyError:
        print("❌ Error: Sweet not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def restock_sweet_cli(inventory):
    """Handle restocking sweets via CLI"""
    print("\n📦 Restock Sweet")
    if not inventory.sweets:
        print("📭 Inventory is empty.")
        return
    
    sweet_id = get_integer_input("Enter sweet ID to restock: ", min_val=1)
    quantity = get_integer_input("Enter quantity to add: ", min_val=1)
    
    try:
        inventory.restock_sweet(sweet_id, quantity)
        print(f"✅ Successfully restocked {quantity} item(s)! 📈")
    except KeyError:
        print("❌ Error: Sweet not found.")
    except ValueError as e:
        print(f"❌ Error: {e}")

def main():
    """Main entry point for the Sweet Shop CLI"""
    inventory = Inventory()
    
    while True:
        display_menu()
        try:
            choice = get_integer_input("\nEnter your choice (0-7): ", min_val=0, max_val=7)
            
            if choice == 0:
                print("\n🚪 Exiting Sweet Shop Management System. Goodbye! 👋")
                break
            elif choice == 1:
                add_sweet_cli(inventory)
            elif choice == 2:
                delete_sweet_cli(inventory)
            elif choice == 3:
                view_all_sweets_cli(inventory)
            elif choice == 4:
                search_sweets_cli(inventory)
            elif choice == 5:
                sort_sweets_cli(inventory)
            elif choice == 6:
                purchase_sweet_cli(inventory)
            elif choice == 7:
                restock_sweet_cli(inventory)
            else:
                print("⚠️ Invalid choice. Please try again.")
        
        except KeyboardInterrupt:
            print("\n⚠️ Operation cancelled. Returning to main menu.")
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()