#Question 1
def calculate_discount(price, discount_percent):
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price


# Question 2 Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(original_price, discount)

# Print results
if discount >= 20:
    print(f"The final price after {discount}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
