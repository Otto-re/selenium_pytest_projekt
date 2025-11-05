Example software: GroceryMate

1. Product Search Functionality

Test Design Techniques: Equivalence Partitioning (EP), Error Guessing

Test Cases:

1. Equivalence Partitioning:

- **Test Case:** Verify product search with valid keyword
  - **Input:** Keyword = "milk"
  - **Expected Outcome:** List of products containing the word "milk" is displayed.

2. Equivalence Partitioning:

- **Test Case:** Verify product search with invalid keyword
  - **Input:** Keyword = "xyz123" (no product matches)
  - **Expected Outcome:** Message "No products found" is displayed.

3. Error Guessing:

- **Test Case:** Verify product search with special characters
  - **Input:** Keyword = "!@#$%"
  - **Expected Outcome:** Message "No products found" is displayed or input is sanitized.2. Shopping Cart Functionality

**Empfohlener Testfall zur Automatisierung:**  
Test Case 1 – Produktsuche mit gültigem Keyword.  
*Grund:* Wiederholbar, klar definiert, hohe Relevanz für Regression Testing.
Test Design Techniques: Use Case Testing, Equivalence Partitioning (EP), Error Guessing

Test Cases:

1. Use Case Testing:

- **Test Case:** Verify that a product can be added to the shopping cart.
  - **Input:** Click "Add to cart" on a product.
  - **Expected Outcome:** Product is added to cart, cart count increases by 1.

2. Equivalence Partitioning:

- **Test Case:** Verify adding multiple different products to the cart.
  - **Input:** Add 3 different products to cart.
  - **Expected Outcome:** All products are listed in the cart.

3. Error Guessing:

- **Test Case:** Verify behavior when trying to add an out-of-stock product.
  - **Input:** Click "Add to cart" on a product with stock = 0.
  - **Expected Outcome:** Error message like "This product is currently unavailable."

---

3. Checkout Process

Test Design Techniques: Use Case Testing, Boundary Value Analysis (BVA), Error Guessing

Test Cases:

1. Use Case Testing:

- **Test Case:** Verify successful checkout with valid address and payment details.
  - **Input:** Enter all valid checkout information and confirm.
  - **Expected Outcome:** Order is placed, confirmation message is displayed.

2. Boundary Value Analysis:

- **Test Case:** Verify behavior with minimum order value (e.g. €1).
  - **Input:** Place order with cart total = €1.
  - **Expected Outcome:** Order is accepted.

3. Error Guessing:

- **Test Case:** Verify checkout with invalid payment details.
  - **Input:** Enter expired credit card information.
  - **Expected Outcome:** Error message "Payment failed. Please check your details."
