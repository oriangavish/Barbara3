from penguin_game import *
from Ratings.rate_enemy_icebergs import rate_enemy_icebergs
from who_should_attack import who_should_attack
from attack import attack

# Function first decides which iceberg to be attacked. Then, we'll iterate over the icebergs that are returned, and see if we already have a penguin group traveling to that iceberg. If not, we choose which iceberg should attack using who_should_attack and then use the attack function to send penguin groups from where we specified. Function will return True if penguins are successfully sent and False if no attacks occur.

def attack_by_rating(game):
    icebergs_to_be_attacked = rate_enemy_icebergs(game)
    our_current_penguin_groups = game.get_my_penguin_groups
    for iceberg_to_attack in icebergs_to_be_attacked:
        for penguin_group in our_current_penguin_groups:
            if penguin_group.destination == iceberg_to_attack:
                icebergs_to_be_attacked.remove(iceberg_to_attack)
    if icebergs_to_be_attacked == []:
        return False
    for iceberg_to_attack in icebergs_to_be_attacked:
        # attacking_icebergs are the icebergs from which the attacking penguin group is sent 
        attacking_icebergs = who_should_attack(game, iceberg_to_attack)

        # If there are multiple icebergs that should attack, than the who_should_attack function will return a list and an attack is done from each iceberg
        if isinstance(attacking_icebergs, list):
            for attacking_iceberg in attacking_icebergs:
                attack(game, attacking_iceberg)
            return True
        else:
            attack(game, attacking_icebergs)
            return True

        
