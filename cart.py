"""
Shopping Cart module for the Supermarket System
Manages items added to the shopping cart
"""


class CartItem:
    """Represents an item in the shopping cart"""
    
    def __init__(self, product, quantity):
        """
        Initialize a cart item
        
        Args:
            product: Product object
            quantity: Quantity of the product
        """
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self):
        """Calculate subtotal for this item"""
        return self.product.price * self.quantity
    
    def __repr__(self):
        return f"{self.product.name} x{self.quantity} = ${self.get_subtotal():.2f}"


class ShoppingCart:
    """Manages the shopping cart"""
    
    def __init__(self):
        """Initialize an empty shopping cart"""
        self.items = {}  # {product_id: CartItem}
    
    def add_item(self, product, quantity=1):
        """
        Add an item to the cart
        
        Args:
            product: Product object to add
            quantity: Quantity to add
        """
        if product.product_id in self.items:
            self.items[product.product_id].quantity += quantity
        else:
            self.items[product.product_id] = CartItem(product, quantity)
    
    def remove_item(self, product_id):
        """
        Remove an item from the cart
        
        Args:
            product_id: ID of the product to remove
            
        Returns:
            True if item was removed, False if not found
        """
        if product_id in self.items:
            del self.items[product_id]
            return True
        return False
    
    def update_quantity(self, product_id, quantity):
        """
        Update the quantity of an item
        
        Args:
            product_id: ID of the product
            quantity: New quantity
            
        Returns:
            True if successful, False if product not in cart
        """
        if product_id in self.items:
            if quantity <= 0:
                self.remove_item(product_id)
            else:
                self.items[product_id].quantity = quantity
            return True
        return False
    
    def get_item_count(self):
        """Get total number of items in cart"""
        return sum(item.quantity for item in self.items.values())
    
    def get_subtotal(self):
        """Calculate subtotal of all items"""
        return sum(item.get_subtotal() for item in self.items.values())
    
    def is_empty(self):
        """Check if cart is empty"""
        return len(self.items) == 0
    
    def display_cart(self):
        """Display cart contents"""
        if self.is_empty():
            print("Your cart is empty!\n")
            return
        
        print("\n" + "="*70)
        print(f"{'Product Name':<30} {'Qty':<5} {'Unit Price':<12} {'Subtotal':<12}")
        print("="*70)
        
        for item in self.items.values():
            print(f"{item.product.name:<30} {item.quantity:<5} ${item.product.price:<11.2f} ${item.get_subtotal():<11.2f}")
        
        print("="*70)
        print(f"{'Subtotal:':<50} ${self.get_subtotal():<11.2f}")
        print("="*70 + "\n")
    
    def clear(self):
        """Clear all items from the cart"""
        self.items.clear()
