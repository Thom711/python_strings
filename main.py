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

report = f"{goal_0_player} scored in the {str(goal_0)}nd minute \n{goal_1_player} scored in the {str(goal_1)}th minute"

# PART 2
player = "Ronald Koeman"

first_name = player[player.find("Ronald"):len("Ronald")]

last_name_len = len(player[player.find("Koeman"):])

name_short = player[player.find("Ronald"):1] + '. ' + player[player.find("Koeman"):]

chant = ((player[player.find("Ronald"):len("Ronald")] + '! ') * 6).strip() 

good_chant = chant[-1] != ' '