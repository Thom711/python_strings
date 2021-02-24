# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# PART 1
goal_0 = 32
goal_0_player = "Ruud Gullit"

goal_1 = 54
goal_1_player = "Marco van Basten"

scorers = goal_0_player + ' ' + str(goal_0) + ', ' + goal_1_player + ' ' + str(goal_1)

report = f"{goal_0_player} scored in the {goal_0}nd minute \n{goal_1_player} scored in the {goal_1}th minute"


# PART 2
player = "Ronald Koeman"

first_name = player[:player.find(' ')]

last_name_len = len(player[player.find(' ')+1:])

name_short = player[0].upper() + '. ' + player[player.find(' ')+1:]

chant = ((player[:player.find(' ')] + '! ') * len(player[:player.find(' ')])).strip()

good_chant = chant[-1] != ' '