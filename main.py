"""
Main module for the Supermarket System
Provides interactive menu-driven interface for users
"""

from supermarket import Supermarket


def display_main_menu():
    """Display the main menu"""
    print("\n" + "="*70)
    print("MAIN MENU".center(70))
    print("="*70)
    print("1. Start Shopping")
    print("2. View Inventory")
    print("3. View Sales Report")
    print("4. Exit")
    print("="*70)


def display_shopping_menu():
    """Display the shopping menu"""
    print("\n" + "-"*70)
    print("SHOPPING MENU".center(70))
    print("-"*70)
    print("1. View Available Products")
    print("2. Add Item to Cart")
    print("3. Remove Item from Cart")
    print("4. View Shopping Cart")
    print("5. Checkout")
    print("6. Cancel Shopping")
    print("-"*70)


def view_products(supermarket):
    """Display all available products"""
    print("\n" + "="*70)
    print(f"{'ID':<5} {'Product Name':<25} {'Price':<10} {'Category':<15} {'Stock':<5}")
    print("="*70)
    
    for product in supermarket.inventory.list_products():
        stock = supermarket.inventory.get_stock(product.product_id)
        status = "✓" if stock > 0 else "OUT"
        print(f"{product.product_id:<5} {product.name:<25} ${product.price:<9.2f} {product.category:<15} {stock:<5} ({status})")
    
    print("="*70 + "\n")


def shopping_session(supermarket):
    """Handle a shopping session"""
    supermarket.start_shopping_session()
    
    while True:
        display_shopping_menu()
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            view_products(supermarket)
        
        elif choice == '2':
            view_products(supermarket)
            try:
                product_id = int(input("Enter Product ID to add: "))
                quantity = int(input("Enter Quantity: "))
                
                if quantity <= 0:
                    print("✗ Quantity must be greater than 0!")
                else:
                    supermarket.add_to_cart(product_id, quantity)
            
            except ValueError:
                print("✗ Invalid input! Please enter numbers only.")
        
        elif choice == '3':
            try:
                product_id = int(input("Enter Product ID to remove: "))
                supermarket.remove_from_cart(product_id)
            except ValueError:
                print("✗ Invalid input! Please enter a number.")
        
        elif choice == '4':
            supermarket.view_cart()
        
        elif choice == '5':
            supermarket.view_cart()
            if not supermarket.current_customer.is_empty():
                print("\nAvailable Payment Methods: Cash, Card, Mobile Payment")
                payment = input("Enter Payment Method (default: Cash): ").strip()
                if not payment:
                    payment = "Cash"
                
                supermarket.checkout(payment)
                break
        
        elif choice == '6':
            print("✗ Shopping cancelled.")
            supermarket.current_customer = None
            break
        
        else:
            print("✗ Invalid choice! Please try again.")


def main():
    """Main function to run the supermarket system"""
    
    # Initialize supermarket
    supermarket = Supermarket("SuperMart")
    supermarket.setup_sample_inventory()
    
    print("\n" + "="*70)
    print(f"Welcome to {supermarket.name}".center(70))
    print("="*70)
    
    while True:
        display_main_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            shopping_session(supermarket)
        
        elif choice == '2':
            supermarket.display_inventory()
        
        elif choice == '3':
            supermarket.display_sales_report()
        
        elif choice == '4':
            print("\nThank you for using SuperMart. Goodbye!\n")
            break
        
        else:
            print("✗ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
