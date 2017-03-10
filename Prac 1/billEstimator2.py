

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator 2\n")
tariff = input("What tariff are you using (11 or 31)?: ")
while tariff not in ["11", "31"]:
    tariff = input("Enter 11 or 31: ")
daily_use_Kwh = float(input("Enter the Kwh used per day: "))
billing_days = int(input("Enter the billing days: "))
if tariff == 11:
    total = (TARIFF_11 * daily_use_Kwh * billing_days) / 100
else:
    total = (TARIFF_31 * daily_use_Kwh * billing_days) / 100
print("\nEstimated Bill will be ${:.2f}".format(total))
