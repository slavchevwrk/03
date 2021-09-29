#Variables
trip_price = float(input())
pcs_puzzle = int(input())
pcs_talking_puppets = int(input())
pcs_teddy_bears = int(input())
pcs_minions = int(input())
pcs_trucks = int(input())

#Pre-defined
price_per_puzzel = 2.60
price_per_talking_pupet = 3
price_per_teddy_bear = 4.10
price_per_minion = 8.20
price_per_truck = 2

#Calculations
total_toys_ordered = pcs_trucks + pcs_puzzle + pcs_minions + pcs_teddy_bears + pcs_talking_puppets

total_money = price_per_puzzel * pcs_puzzle + price_per_talking_pupet * pcs_talking_puppets + price_per_teddy_bear *\
              pcs_teddy_bears + price_per_minion * pcs_minions + price_per_truck * pcs_trucks

if total_toys_ordered >= 50:
    discount = total_money * 0.25
    total_money = total_money - discount
    money_left = total_money - total_money * 0.1
else:
    money_left = total_money - total_money * 0.1

if money_left >= trip_price:
    money_left -= trip_price
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_left = trip_price - money_left
    print(f"Not enough money! {money_left:.2f} lv needed.")