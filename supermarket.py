"""
Supermarket module for the Supermarket System
Main supermarket class that manages the entire system
"""

from datetime import datetime
from inventory import Inventory
from cart import ShoppingCart
from product import Product


class Supermarket:
    """Main supermarket class managing inventory, sales, and customers"""
    
    def __init__(self, name):
        """
        Initialize a supermarket
        
        Args:
            name: Name of the supermarket
        """
        self.name = name
        self.inventory = Inventory()
        self.sales = []  # List of completed transactions
        self.current_customer = None
    
    def setup_sample_inventory(self):
        """Set up sample products for demonstration"""
        # Fruits & Vegetables
        self.inventory.add_product(Product(1, "Apple", 1.50, "Fruits"), 50)
        self.inventory.add_product(Product(2, "Banana", 0.99, "Fruits"), 60)
        self.inventory.add_product(Product(3, "Carrot", 0.75, "Vegetables"), 40)
        self.inventory.add_product(Product(4, "Tomato", 1.25, "Vegetables"), 35)
        
        # Dairy
        self.inventory.add_product(Product(5, "Milk (1L)", 3.50, "Dairy"), 30)
        self.inventory.add_product(Product(6, "Cheese", 5.99, "Dairy"), 20)
        self.inventory.add_product(Product(7, "Yogurt", 2.99, "Dairy"), 25)
        
        # Bakery
        self.inventory.add_product(Product(8, "Bread", 2.50, "Bakery"), 40)
        self.inventory.add_product(Product(9, "Donut", 1.99, "Bakery"), 35)
        
        # Beverages
        self.inventory.add_product(Product(10, "Orange Juice (1L)", 4.99, "Beverages"), 25)
        self.inventory.add_product(Product(11, "Coffee (500g)", 8.99, "Beverages"), 20)
    
    def start_shopping_session(self):
        """Start a new shopping session"""
        self.current_customer = ShoppingCart()
        print(f"\n{'='*70}")
        print(f"Welcome to {self.name}!")
        print(f"{'='*70}\n")
    
    def add_to_cart(self, product_id, quantity=1):
        """
        Add a product to the current customer's cart
        
        Args:
            product_id: ID of the product
            quantity: Quantity to add
            
        Returns:
            True if successful, False otherwise
        """
        if self.current_customer is None:
            print("Start a shopping session first!")
            return False
        
        product = self.inventory.get_product(product_id)
        
        if product is None:
            print(f"✗ Product ID {product_id} not found!")
            return False
        
        if not self.inventory.is_available(product_id, quantity):
            available = self.inventory.get_stock(product_id)
            print(f"✗ Only {available} units of '{product.name}' available!")
            return False
        
        self.current_customer.add_item(product, quantity)
        print(f"✓ Added {quantity} x {product.name} to cart")
        return True
    
    def remove_from_cart(self, product_id):
        """
        Remove a product from the cart
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            True if successful, False otherwise
        """
        if self.current_customer is None:
            print("Start a shopping session first!")
            return False
        
        product = self.inventory.get_product(product_id)
        if product is None:
            print(f"✗ Product ID {product_id} not found!")
            return False
        
        if self.current_customer.remove_item(product_id):
            print(f"✓ Removed {product.name} from cart")
            return True
        else:
            print(f"✗ {product.name} not in cart!")
            return False
    
    def view_cart(self):
        """Display the current shopping cart"""
        if self.current_customer is None:
            print("Start a shopping session first!")
            return
        
        self.current_customer.display_cart()
    
    def checkout(self, payment_method="Cash"):
        """
        Process checkout for the current customer
        
        Args:
            payment_method: Method of payment
            
        Returns:
            Transaction details or None if checkout failed
        """
        if self.current_customer is None:
            print("Start a shopping session first!")
            return None
        
        if self.current_customer.is_empty():
            print("✗ Cart is empty! Cannot checkout.")
            return None
        
        # Process payment
        total = self.current_customer.get_subtotal()
        tax_rate = 0.08  # 8% tax
        tax = total * tax_rate
        final_total = total + tax
        
        # Update inventory
        for product_id, item in self.current_customer.items.items():
            self.inventory.reduce_stock(product_id, item.quantity)
        
        # Record transaction
        transaction = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'items': len(self.current_customer.items),
            'subtotal': total,
            'tax': tax,
            'total': final_total,
            'payment_method': payment_method,
            'products': [(item.product.name, item.quantity) for item in self.current_customer.items.values()]
        }
        self.sales.append(transaction)
        
        # Display receipt
        self.print_receipt(transaction)
        
        # Reset cart for next customer
        self.current_customer = None
        return transaction
    
    def print_receipt(self, transaction):
        """Print a receipt for a transaction"""
        print("\n" + "="*70)
        print(f"{self.name} - RECEIPT".center(70))
        print("="*70)
        print(f"Date & Time: {transaction['timestamp']}")
        print("-"*70)
        
        for product_name, quantity in transaction['products']:
            print(f"  {product_name:<45} x{quantity}")
        
        print("-"*70)
        print(f"Subtotal: {' '*40} ${transaction['subtotal']:<10.2f}")
        print(f"Tax (8%): {' '*40} ${transaction['tax']:<10.2f}")
        print("="*70)
        print(f"TOTAL: {' '*47} ${transaction['total']:<10.2f}")
        print("="*70)
        print(f"Payment Method: {transaction['payment_method']}")
        print("Thank you for shopping at " + self.name + "!")
        print("="*70 + "\n")
    
    def display_sales_report(self):
        """Display sales report"""
        if not self.sales:
            print("No sales recorded yet!\n")
            return
        
        total_revenue = sum(sale['total'] for sale in self.sales)
        total_transactions = len(self.sales)
        avg_transaction = total_revenue / total_transactions if total_transactions > 0 else 0
        
        print("\n" + "="*70)
        print(f"{self.name} - SALES REPORT".center(70))
        print("="*70)
        print(f"Total Transactions: {total_transactions}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print(f"Average Transaction Value: ${avg_transaction:.2f}")
        print("="*70 + "\n")
    
    def display_inventory(self):
        """Display current inventory"""
        print(f"\n{self.name} - INVENTORY")
        self.inventory.display_inventory()
