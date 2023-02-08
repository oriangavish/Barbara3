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
   attack_count = 0
   for iceberg_to_attack in icebergs_to_be_attacked:
       # The iceberg that does the attack is chosen with the function attack() and adds +1 to the attack count if the attack was successfully sent.
       if attack(iceberg_to_attack):
           attack_count += 1
   if attack_count > 0:
       return True
   return False