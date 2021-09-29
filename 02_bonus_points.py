number = int(input())

if number <= 100:
    bonus = 5

elif number <= 1000:
    bonus = number * 0.2

else:
    bonus = number * 0.1

if number % 2 == 0:
        bonus = bonus + 1

elif number % 10 == 5:
        bonus = bonus + 2

total_bonus = bonus
total_points = total_bonus + number

print(total_bonus)
print(total_points)