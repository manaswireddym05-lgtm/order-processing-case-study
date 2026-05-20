# Custom Exception for managing invalid orders
class InvalidOrderError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def calculate_bill(price, qty):
    """Calculates the mathematical total cost."""
    return price * qty

def process_order(order_str):
    """Parses individual order strings and handles validations."""
    parts = order_str.split(',')
    
    # 1. Structural Check: Must have Name, Price, and Quantity
    if len(parts) != 3:
        raise InvalidOrderError(f"Format Error: Expected 3 values, got {len(parts)} -> '{order_str}'")
        
    product_name = parts[0].strip()
    price_raw = parts[1].strip()
    qty_raw = parts[2].strip()
    
    # 2. Completeness Check: Ensure fields aren't empty strings
    if not product_name or not price_raw or not qty_raw:
        raise InvalidOrderError(f"Missing Data Error: One or more fields are empty -> '{order_str}'")
    
    # 3. Type Conversion Check: Price and Qty must be numeric
    try:
        price = float(price_raw)
        qty = int(qty_raw)
    except ValueError:
        raise InvalidOrderError(f"Data Type Error: Non-numeric value found in price/quantity -> '{order_str}'")
        
    # Calculate final bill if all checks pass
    total_cost = calculate_bill(price, qty)
    print(f"✅ Success: {product_name} | Total Cost: ${total_cost:,.2f}")

# --- Driver Script Execution ---
if __name__ == "__main__":
    orders = [
        "Laptop,55000,2",
        "Mobile,abc,1",
        "Tablet,20000,3",
        "Camera,45000",
        "Headphones,20000,2",
        "TV,70000,1",
        "Mouse,500,5",
        "Keyboard,1500,2",
        "Charger,800,",
        "INVALID"
    ]

    print("--- Processing System Log ---")
    for order in orders:
        try:
            process_order(order)
        except InvalidOrderError as e:
            print(f"❌ Error Logged: {e.message}")
          
