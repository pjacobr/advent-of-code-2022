# puzzle 1 - Elf Calories
# get elves and number of calories per elf
lines = input.splitlines()
# go through each line and add up until spaces
elves = []
sum = 0
for line in lines:
    if line == '':
        elves.append(sum)
        sum = 0
    else:
        sum += int(line)
elves.append(sum)

# get the max number of calories
max_calories = max(elves)

print(max_calories)

# get the top 3 numbers
top3 = sorted(elves, reverse=True)[:3]

# sum those numbers
sum = 0
for num in top3:
    sum += num

print(sum)