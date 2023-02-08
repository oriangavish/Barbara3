from penguin_game import *
from check_if_attacked_i import check_if_attacked_i

# First checks to see if the iceberg is even being attacked. If yes, makes sure that it contains the proper amount of penguins on the iceberg to defend itself by the time the enemy group arrives.
def check_if_safe_I(game, iceberg):
    if check_if_attacked_i(iceberg, game) == False:
        return True
    enemy_groups = game.get_enemy_penguin_groups
    for enemy_group in enemy_groups:
        if enemy_group.destination == iceberg:
            target = enemy_group.destination
            turns_till_arrival = enemy_group.turns_till_arrival
            additional_penguins = target.penguins_per_turn * turns_till_arrival
            if enemy_group.penguin_amount < (target.penguin_amount + additional_penguins + 1):
                return True
    return False