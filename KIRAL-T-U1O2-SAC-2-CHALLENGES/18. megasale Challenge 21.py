customer_spent = float(input("How much did the customer spend? "))
if customer_spent > 20:
    print("$3 voucher.")
elif customer_spent > 10:
    print("$1 voucher.")
else:
    print("No voucher.")
    