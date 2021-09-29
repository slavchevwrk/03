#Variables
budget = float(input())
extras = int(input())
clothing_price = float(input())

#Calculations
decor = budget * 0.1

if extras >= 150:
    clothing_price -= clothing_price * 0.1

total_money_needed = extras * clothing_price + decor
difference = abs(total_money_needed - budget)
if total_money_needed > budget:
    budget -= difference
    print("Not enough money!")
    print(f"Wingard needs {budget:2f} leva more.")
else:
    budget -= difference
    print("Action!")
    print(f"Wingard starts filming with {budget:.2f} leva left.")