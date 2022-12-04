with open('input-problem3.txt', 'r') as file:
    data = file.read()

lines = data.splitlines()

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52

# get the ascii value of the letter
def get_value_of_letter(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26
points = 0
for line in lines:
    first_half, second_half = line[len(line)//2:], line[:len(line)//2]
    first_half_letters = set(first_half)
    second_half_letters = set(second_half)
    common_letters = first_half_letters.intersection(second_half_letters)
    for letter in common_letters:
        points += get_value_of_letter(letter)


# part two
points = 0
for i in range(0, len(lines), 3):
    line_one_letters = set(lines[i])
    line_two_letters = set(lines[i+1])
    line_three_letters = set(lines[i+2])
    common_letters = line_one_letters.intersection(line_two_letters, line_three_letters)
    group_letter = common_letters.pop()
    points += get_value_of_letter(group_letter)