# Rock paper scissors
import random
# We need to take users choice, r, p, s
# We need to generate computer's choice
# Compare both choice 
# if statements
# result
while (True):

	user_choice = input("Enter your choice: r for rock, s for scissors, p for paper ")

	comp_choice = random.randint(1, 3)
	if (comp_choice == 1):
		comp_choice = "r"
	elif (comp_choice == 2):
		comp_choice = "s"
	else:
		comp_choice = "p"

	print("Computer chose : " + str(comp_choice))

	if (user_choice == 'p' and comp_choice == 's'):
		print("Computer won")
	elif (user_choice == 'r' and comp_choice == 'p'):
		print("Computer won")
	elif (user_choice == 's' and comp_choice == 'r'):
		print("Computer won")
	elif (user_choice == 'p' and comp_choice == 'r'):
		print("You won")
	elif (user_choice == 's' and comp_choice == 'p'):
		print("You won")
	elif (user_choice == 'r' and comp_choice == 's'):
		print("You won")
	else:
		print("Its a tie")