"""
Week 3 Task: Practical Code Analysis and Debugging Exercise

This beginner-friendly example demonstrates common errors in a small
shopping-total program. The original buggy version is documented in the
report. This file contains the corrected, runnable version.

Run:
    python code_analysis_debugging.py
"""

def calculate_total(prices, discount_percent=0):
    """Return the total after applying a percentage discount.

    Args:
        prices: An iterable of non-negative numeric item prices.
        discount_percent: Discount percentage from 0 to 100.

    Returns:
        The discounted total as a float.

    Raises:
        TypeError: If prices or discount are not numeric as expected.
        ValueError: If a price is negative or discount is out of range.
    """
    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100.")

    total = 0.0
    for price in prices:
        if not isinstance(price, (int, float)):
            raise TypeError("Every price must be a number.")
        if price < 0:
            raise ValueError("Prices cannot be negative.")
        total += price

    discount = total * (discount_percent / 100)
    final_total = total - discount
    return round(final_total, 2)


def main():
    """Collect sample prices, calculate the total, and display results."""
    prices = [120.00, 80.00, 50.00]
    discount_percent = 10

    try:
        total_before_discount = sum(prices)
        final_total = calculate_total(prices, discount_percent)

        print("Shopping Total Calculator")
        print("-------------------------")
        print(f"Items: {len(prices)}")
        print(f"Subtotal: ₹{total_before_discount:.2f}")
        print(f"Discount: {discount_percent}%")
        print(f"Final total: ₹{final_total:.2f}")
    except (TypeError, ValueError) as error:
        print(f"Input error: {error}")


if __name__ == "__main__":
    main()
