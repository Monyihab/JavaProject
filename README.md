# Supermarket Management System

A comprehensive Python-based supermarket management system that allows customers to browse products, manage shopping carts, and complete purchases, while also tracking inventory and sales.

## Features

### 🛒 Shopping Features
- **Browse Products**: View all available products with prices and stock levels
- **Shopping Cart Management**: Add, remove, and update product quantities
- **Checkout System**: Process payments with multiple payment methods
- **Receipt Generation**: Automatic receipt printing after purchase

### 📦 Inventory Management
- **Product Catalog**: Organize products by category (Fruits, Vegetables, Dairy, Bakery, Beverages)
- **Stock Tracking**: Real-time inventory updates
- **Stock Availability**: Check product availability before adding to cart

### 📊 Business Analytics
- **Sales Reporting**: Track total revenue, number of transactions, and average transaction value
- **Transaction History**: Record all completed sales with timestamps and payment details
- **Tax Calculation**: Automatic 8% tax calculation on all purchases

## Project Structure

```
supermarket_system/
├── product.py          # Product class definition
├── inventory.py        # Inventory management system
├── cart.py            # Shopping cart and cart items
├── supermarket.py     # Main supermarket class
├── main.py            # Interactive menu interface
└── README.md          # This file
```

## How to Run

### Prerequisites
- Python 3.6 or higher

### Installation
No external dependencies required! The system uses only Python's standard library.

### Running the Application

```bash
python main.py
```

Or on Windows:
```bash
python main.py
```

## Usage Guide

### Main Menu Options

1. **Start Shopping**: Begin a new shopping session
2. **View Inventory**: See all products and their stock levels
3. **View Sales Report**: Check business statistics
4. **Exit**: Close the application

### Shopping Session

Once you start shopping:
1. **View Available Products**: Browse the complete product catalog
2. **Add Item to Cart**: Select a product ID and quantity
3. **Remove Item from Cart**: Remove products you don't want
4. **View Shopping Cart**: See all items, prices, and subtotal
5. **Checkout**: Proceed with payment and get receipt
6. **Cancel Shopping**: Exit the shopping session

## Sample Inventory

The system comes preloaded with sample products:

### Fruits
- Apple: $1.50
- Banana: $0.99

### Vegetables
- Carrot: $0.75
- Tomato: $1.25

### Dairy
- Milk (1L): $3.50
- Cheese: $5.99
- Yogurt: $2.99

### Bakery
- Bread: $2.50
- Donut: $1.99

### Beverages
- Orange Juice (1L): $4.99
- Coffee (500g): $8.99

## Class Overview

### Product Class
Represents individual products with ID, name, price, and category.

### Inventory Class
Manages product stock, availability checks, and stock updates.

### CartItem Class
Represents items in the shopping cart with quantity and subtotal calculation.

### ShoppingCart Class
Manages the customer's shopping cart with add, remove, and total calculation methods.

### Supermarket Class
Main class that orchestrates:
- Inventory management
- Shopping sessions
- Checkout and payment processing
- Sales tracking and reporting

## Key Features Explained

### Cart Management
- Add multiple quantities of the same product
- Update quantities for existing items
- Remove items from cart
- Clear cart before checkout

### Stock Management
- Inventory reduces automatically after checkout
- Prevents overselling by checking stock before adding to cart
- Real-time availability status display

### Payment & Receipt
- Supports multiple payment methods (Cash, Card, Mobile Payment)
- Automatic 8% tax calculation
- Detailed receipt printing with timestamp
- Transaction history tracking

## Example Walkthrough

1. Run `python main.py`
2. Select option "1" to start shopping
3. Choose "1" to view products
4. Add items by selecting option "2" and entering product IDs
5. View your cart with option "4"
6. Proceed to checkout with option "5"
7. Select a payment method
8. View receipt and complete transaction

## Future Enhancements

Potential improvements to the system:
- Customer loyalty program
- Discount codes and coupons
- Product search and filtering
- Database integration for persistent storage
- Barcode scanning functionality
- Employee management system
- Advanced reporting and analytics
- Multi-store management

## Notes

- All prices are in USD
- Tax rate is fixed at 8%
- Stock quantities are limited to the sample data
- All data is stored in memory (lost on program exit)

## License

This project is open source and available for educational purposes.

---

**Created**: 2024
**Version**: 1.0
