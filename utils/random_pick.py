#------------------------------------------------------------------------------
#RANDOM PICK
#------------------------------------------------------------------------------

#Simple function just randomly picks a hint from the hint / tip list for the main menu.

#------------------------------------------------------------------------------
#libraries
#------------------------------------------------------------------------------
import random 

#------------------------------------------------------------------------------
#random pick function
#------------------------------------------------------------------------------
def rand_item(pick_list):
    return random.choice(pick_list) #Choose something random within the list given in the paremeter.