# Program to calculate electricity bill based on units consumed

units = float(input("Enter number of units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

print(f"Total electricity bill: ₹{bill:.2f}")
