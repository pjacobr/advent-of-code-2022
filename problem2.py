# read in text file into variable

with open('input-problem2.txt', 'r') as file:
    data = file.read()

# command list
commands = data.splitlines()

opponent_command_map = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

player_command_map = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

move_score_map = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}

win_scenarios = [
    ("Rock", "Scissors"),
    ("Paper", "Rock"),
    ("Scissors", "Paper"),
]


move_score = 0
round_score = 0
for line in commands:
    opponent_command, player_command = line.split(' ')

    opponent_move = opponent_command_map[opponent_command]
    player_move = player_command_map[player_command]

    move_score += move_score_map[player_move]

    # Draw
    if opponent_move == player_move:
        print(player_move,opponent_move, "Draw")
        round_score += 3
    # Win
    elif (player_move, opponent_move) in win_scenarios:
        print(player_move,opponent_move, "Win")
        round_score += 6
    # Lose
    else:
        print(player_move,opponent_move, "Lose")
        round_score += 0

print(move_score + round_score)


# Part 2
# X = Lose, Y = Draw, Z = Win
move_score = 0
round_score = 0


def get_losing_move(move):
    """Get the move that would lose to the given move"""
    if move == "Rock":
        return "Scissors"
    elif move == "Paper":
        return "Rock"
    elif move == "Scissors":
        return "Paper"


def get_winning_move(move):
    """Get the move that would win to the given move"""
    if move == "Rock":
        return "Paper"
    elif move == "Paper":
        return "Scissors"
    elif move == "Scissors":
        return "Rock"

move_score = 0
round_score = 0
for line in commands:
    opponent_command, player_command = line.split(' ')

    opponent_move = opponent_command_map[opponent_command]
    if player_command == "X":
        # choose losing move
        player_move = get_losing_move(opponent_move)
    elif player_command == "Y":
        # choose draw move
        player_move = opponent_move
    elif player_command == "Z":
        # choose winning move
        player_move = get_winning_move(opponent_move)

    move_score += move_score_map[player_move]

    # Draw
    if opponent_move == player_move:
        print(player_move,opponent_move, "Draw")
        round_score += 3
    # Win
    elif (player_move, opponent_move) in win_scenarios:
        print(player_move,opponent_move, "Win")
        round_score += 6
    # Lose
    else:
        print(player_move,opponent_move, "Lose")
        round_score += 0

print(move_score + round_score)