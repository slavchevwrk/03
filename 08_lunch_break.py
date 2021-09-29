from math import ceil
#Variables
series_name = str(input())
episode_lenght = int(input())
lunch_break_lenght = int(input())

#Calculations
lunch_time =  lunch_break_lenght * 1 / 8
rest_time = lunch_break_lenght * 1 / 4
total_time_needed = episode_lenght + lunch_time + rest_time
difference = abs(lunch_break_lenght - total_time_needed)
difference = ceil(difference)

if lunch_break_lenght >= total_time_needed:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")