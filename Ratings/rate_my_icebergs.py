from penguin_game import *
from Defense.check_if_safe_I import *


def rate_iceberg(iceberg, game):
    # Calculates distances from home base and enemy base
    distance_from_home = iceberg.get_turns_till_arrival(game.get_my_icepital_icebergs[0])
    distance_from_enemy = iceberg.get_turns_till_arrival(game.get_enemy_icepital_icebergs[0])
    per_turn = iceberg.penguins_per_turn

    # the closer the iceberg to our base or theirs, the higher the rating.
    # Distance from our base is more important for defense so will contribute more to rating.
    # Plus take into consideration amount of penguins produced in that iceberg by turn.
    return 20 / distance_from_home + 10 / distance_from_enemy + per_turn


def rate_my_attacked_icebergs(attacked_icebergs, game):
    # Function checks if iceberg can defend itself. If not, it is rated and icebergs requiring defense will be added to
    # a list of icebergs we should defend.
    icebergs_to_be_defended = []
    for iceberg in attacked_icebergs:
        safe = check_if_safe_I(game, iceberg)
        if not safe:
            iceberg_rating = rate_iceberg(iceberg, game)
            if iceberg_rating > 20:
                icebergs_to_be_defended.append(icebergs_to_be_defended)


def rate_for_upgrade(game):
    # returns the best iceberg to upgrade

    icebergs_to_update = []
    for iceberg in game.get_my_icebergs():

        distance_from_home = iceberg.get_turns_till_arrival(game.get_my_icepital_icebergs[0])
        distance_from_enemy = iceberg.get_turns_till_arrival(game.get_enemy_icepital_icebergs[0])
        per_turn = iceberg.penguins_per_turn

        # prioritizes upgrading the closest icebergs to our capital or to enemy capital with the least per_turn first
        # lower score = upgrade first

        if (distance_from_home < distance_from_enemy):
            rating = distance_from_home + per_turn
        else:
            rating = distance_from_enemy + per_turn
        icebergs_to_update.append(rating)
    icebergs_to_update.sort()

    i = 0
    for iceberg in game.get_my_icebergs():
        distance_from_home = iceberg.get_turns_till_arrival(game.get_my_icepital_icebergs[0])
        distance_from_enemy = iceberg.get_turns_till_arrival(game.get_enemy_icepital_icebergs[0])
        per_turn = iceberg.penguins_per_turn
        if (distance_from_home < distance_from_enemy):
            rating = distance_from_home + per_turn
        else:
            rating = distance_from_enemy + per_turn

        if rating == icebergs_to_update[i]:
            return iceberg
        i += 1
    return None
