"""
Product module for the Supermarket System
Defines the Product class representing items available in the supermarket
"""


class Product:
    """Represents a product in the supermarket"""
    
    def __init__(self, product_id, name, price, category):
        """
        Initialize a product
        
        Args:
            product_id: Unique identifier for the product
            name: Name of the product
            price: Price of the product
            category: Category the product belongs to
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
    
    def __repr__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Category: {self.category})"
    
    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"
