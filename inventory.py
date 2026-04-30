"""
Inventory module for the Supermarket System
Manages product stock and inventory operations
"""

from product import Product


class Inventory:
    """Manages the inventory of products in the supermarket"""
    
    def __init__(self):
        """Initialize an empty inventory"""
        self.products = {}  # {product_id: Product}
        self.stock = {}     # {product_id: quantity}
    
    def add_product(self, product, quantity=0):
        """
        Add a new product to inventory
        
        Args:
            product: Product object to add
            quantity: Initial stock quantity
        """
        if product.product_id in self.products:
            print(f"Product {product.product_id} already exists. Updating stock.")
            self.stock[product.product_id] += quantity
        else:
            self.products[product.product_id] = product
            self.stock[product.product_id] = quantity
        print(f"✓ Added {product.name} (Quantity: {quantity})")
    
    def get_product(self, product_id):
        """
        Get a product by ID
        
        Args:
            product_id: ID of the product to retrieve
            
        Returns:
            Product object or None if not found
        """
        return self.products.get(product_id)
    
    def get_stock(self, product_id):
        """
        Get the stock quantity of a product
        
        Args:
            product_id: ID of the product
            
        Returns:
            Stock quantity or 0 if product not found
        """
        return self.stock.get(product_id, 0)
    
    def is_available(self, product_id, quantity=1):
        """
        Check if a product is available in the required quantity
        
        Args:
            product_id: ID of the product
            quantity: Required quantity
            
        Returns:
            True if product is available in required quantity, False otherwise
        """
        return self.get_stock(product_id) >= quantity
    
    def reduce_stock(self, product_id, quantity):
        """
        Reduce the stock of a product
        
        Args:
            product_id: ID of the product
            quantity: Quantity to reduce
            
        Returns:
            True if successful, False otherwise
        """
        if self.is_available(product_id, quantity):
            self.stock[product_id] -= quantity
            return True
        return False
    
    def increase_stock(self, product_id, quantity):
        """
        Increase the stock of a product
        
        Args:
            product_id: ID of the product
            quantity: Quantity to add
        """
        if product_id in self.stock:
            self.stock[product_id] += quantity
    
    def display_inventory(self):
        """Display all products and their stock levels"""
        if not self.products:
            print("Inventory is empty!")
            return
        
        print("\n" + "="*70)
        print(f"{'ID':<5} {'Product Name':<25} {'Price':<10} {'Category':<15} {'Stock':<5}")
        print("="*70)
        
        for product_id, product in self.products.items():
            stock = self.get_stock(product_id)
            status = "✓" if stock > 0 else "✗"
            print(f"{product_id:<5} {product.name:<25} ${product.price:<9.2f} {product.category:<15} {stock:<5} {status}")
        
        print("="*70 + "\n")
    
    def list_products(self):
        """Return list of all available products"""
        return list(self.products.values())
