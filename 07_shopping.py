budget = float(input())
pcs_gpu = int(input())
pcs_cpu = int(input())
pcs_ram = int(input())

gpu_price = 250
cpu_price = (pcs_gpu * gpu_price) * 0.35
ram_price = (pcs_gpu * gpu_price) * 0.1

total_money_needed = pcs_gpu * gpu_price + pcs_cpu * cpu_price + pcs_ram * ram_price
if pcs_gpu > pcs_cpu:
    total_money_needed -= total_money_needed * 0.15

difference = abs(budget - total_money_needed)

if total_money_needed <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")