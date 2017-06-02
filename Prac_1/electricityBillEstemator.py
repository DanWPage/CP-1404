

print("Electricity Bill Estimator\n")
cents_per_Kwh = float(input("Enter the cents per Kwh: "))
daily_use_Kwh = float(input("Enter the Kwh used per day: "))
billing_days = int(input("Enter the billing days: "))

total = (cents_per_Kwh * daily_use_Kwh * billing_days) / 100
print("\nEstimated total bill is ${:.2f}" .format(total))
