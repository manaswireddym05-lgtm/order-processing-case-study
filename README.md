# order-processing-case-study
" A Python-based order processing system that parses transaction data,calculates order totals,and implements custom exception handling for invalid entries."

## 📄 Introduction
In real-world applications, data received from external sources (like CSV files, web forms, or APIs) is frequently messy, incomplete, or incorrectly formatted. This project implements a Python-based **Order Processing System** designed to simulate an automated backend billing pipeline. The application reads string-formatted transaction entries, parses them into usable data types, computes total bills, and gracefully manages malformed entries without crashing.

---

## 🎯 Objectives
* **Data Parsing:** Extract structured fields (Product Name, Price, and Quantity) from comma-separated raw strings.
* **Custom Exception Handling:** Implement a user-defined exception (`InvalidOrderError`) to isolate corrupt or incomplete records.
* **Fault-Tolerant Processing:** Iterate through a batch of mixed-quality orders, rendering valid totals while capturing descriptive errors for invalid lines.
* **Data Type Validation:** Ensure numeric operations are safely guarded against non-numeric data fields (e.g., string values instead of integers).

---

## 📋 Plan of Action
1. **Define Custom Exception:** Create an `InvalidOrderError` class inheriting from Python's built-in `Exception`.
2. **Implement Calculation Engine:** Write `calculate_bill(price, qty)` to mathematically compute the total cost.
3. **Develop Parser & Validator:** Build `process_order(order)` to:
   * Split the input string by commas.
   * Validate that exactly 3 attributes exist (Name, Price, Qty).
   * Convert price and quantity string values to numeric types.
   * Catch `ValueError` or structural issues and raise `InvalidOrderError`.
4. **Execute Driver Pipeline:** Loop through the sample dataset inside a robust `try-except` block to generate the final execution log.

---

## 💻 Source Code
Below is the complete Python solution matching the architectural guidelines:

```python
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
    # Split the comma-separated string
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
