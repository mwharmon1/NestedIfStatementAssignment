"""Author: Michael Harmon
   Last Date Modified: 9/18/2019
   Description: This program has a function that
   will take in 3 values, price, cash, and percent coupon
   and return the total including shipping and tax."""


def calculate_order(price, cash_coupon, percent_coupon):
    TAX = 0.06
    # shipping rates
    UP_TO_TEN_DOLLARS = 5.95

    total_after_cash_coupon = price - cash_coupon
    total_of_percent_off = total_after_cash_coupon * percent_coupon
    total_after_percent_coupon = total_after_cash_coupon - total_of_percent_off
    total_to_add_to_tax = total_after_percent_coupon * TAX
    total_after_tax = total_after_percent_coupon + total_to_add_to_tax
    if total_after_tax < 10.00:
        total = total_after_tax + UP_TO_TEN_DOLLARS
    return round(total, 2)


if __name__ == '__main__':
    item_price = 25.00
    cash_coup = 5.00
    percent_coup = .10
    grand_total = calculate_order(item_price, cash_coup, percent_coup)

    print(grand_total)
