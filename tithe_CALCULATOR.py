def tithe_calc(income, tithe_percent=10):
    """Simple tithe calculator function"""
    tithe = income * (1 * 0.01 * tithe_percent)
    tithe = round(tithe, 2)
    # You may choose to add your own currency in the print output below.
    print(f"With an income of ₦{income:,} and your intention to offer {tithe_percent}%,"
          f" your tithe is ₦{tithe:,} only.")



# Test the function
# tithe_calc(428000.45, 10)
