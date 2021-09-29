hours = int(input())
minutes = int(input())
total_minutes = minutes + 15
if total_minutes > 59:
    hours = hours + 1
    minutes = total_minutes - 60
else:
    minutes = minutes + 15

if hours > 23:
    hours = 0
else:
    pass

if minutes < 10:
    print(f'{hours}:0{minutes}')
else:
    print(f'{hours}:{minutes}')