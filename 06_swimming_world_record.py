current_record = float(input())
distance = float(input())
swimming_speed = float(input())

total_seconds_slowdown = distance // 15 *12.5

ivans_time = distance * swimming_speed + total_seconds_slowdown
difference = abs(current_record - ivans_time)

if current_record > ivans_time:
    print(f" Yes, he succeeded! The new world record is {ivans_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")