from penguin_game import *


def rate_iceberg(iceberg, game):
    # Calculates distances from home base and enemy base
    distance_from_home = iceberg.get_turns_till_arrival(game.get_my_icepital_icebergs[0])
    distance_from_enemy = iceberg.get_turns_till_arrival(game.get_enemy_icepital_icebergs[0])
    per_turn = iceberg.penguins_per_turn

    # the closer the iceberg to our base or theirs, the higher the rating.
    # Plus take into consideration amount of penguins produced in that iceberg by turn.
    return 10 / distance_from_home + 20 / distance_from_enemy + per_turn


def rate_enemy_icebergs(game):
    # Returns list of icebergs that should be attacked
    icebergs_to_be_attacked = []
    for iceberg in game.get_enemy_icebergs():
        rating = rate_iceberg(iceberg, game)
        if rating > 20:
            icebergs_to_be_attacked.append(iceberg)


