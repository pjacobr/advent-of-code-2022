with open('input-problem5.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()

def get_crates(line):
    crates = []
    for i in range(0, len(line), 4):
        if line[i] == ' ':
            crates.append("")
        else:
            crates.append(line[i+1])
    return crates

crate_lines = []
for line in lines:
    if any([c.isnumeric() for c in line.split(" ")]):
        break

    crates = get_crates(line)
    crate_lines.append(crates)

from queue import LifoQueue

stacks = []
for i in range(len(crate_lines[0])):
    stacks.append(LifoQueue())

for i in range(len(crate_lines)-1, -1, -1):
    for j in range(len(crate_lines[i])):
        if crate_lines[i][j] != "":
            stacks[j].put(crate_lines[i][j])

# follow move instructions
for line in lines[len(crate_lines)+2:]:
    quantity, stack1_index, stack2_index = [int(val) for val in line.split(" ") if val.isnumeric()]
    for _ in range(quantity):
        stacks[stack2_index-1].put(stacks[stack1_index-1].get())


for stack in stacks:
    print(stack.get())

# part 2
for line in lines[len(crate_lines)+2:]:
    quantity, stack1_index, stack2_index = [int(val) for val in line.split(" ") if val.isnumeric()]
    temp = []
    for _ in range(quantity):
        temp.append(stacks[stack1_index-1].get())

    for crate in temp[::-1]:
        stacks[stack2_index-1].put(crate)

for stack in stacks:
    print(stack.get())