# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#playernames
player = "Ronald Koeman"
player0 = "Ruud Gullit"
player1 = "Marco van Basten"
#goaltimes
goal_0 = 32
goal_1 = 54

#score message
scorers = player0 + " " +  str(goal_0) + ", " + player1 + " " +  str(goal_1)

#report message
report = player0 + " scored in the " + str(goal_0) + "nd minute\n" + player1 + " scored in the " + str(goal_1) + "th minute"

#first name
first_space_loc = player.find(" ")
first_name = player[:first_space_loc]


#last name
last_name_loc = player.find(" ") + 1
stringlenght = len(player)
last_name = player[last_name_loc : stringlenght]

#short version of name
name_short = first_name[0] + ". " + last_name

#chant
chant = (first_name + "! ") * (len(first_name) - 1) + first_name + "!"

#check the last name length
last_name_len = len(last_name)

#check chant
good_chant = chant != " "
