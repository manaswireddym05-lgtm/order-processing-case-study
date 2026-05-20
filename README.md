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



