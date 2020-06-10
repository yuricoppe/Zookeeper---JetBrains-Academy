initial_amount = int(input())
final_amount = int(input())
half_life = 12
count = 0

while initial_amount > final_amount:
    initial_amount = initial_amount / 2
    count += 1

print(count * half_life)