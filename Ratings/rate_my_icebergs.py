from penguin_game import *


def rate_iceberg(iceberg, game):
    distance_from_home = iceberg.get_turns_till_arrival(game.get_my_icepital_icebergs[0])
    distance_from_enemy = iceberg.get_turns_till_arrival(game.get_enemy_icepital_icebergs[0])
    per_turn = iceberg.penguins_per_turn

    return 20 / distance_from_home + 10 / distance_from_enemy + per_turn


def rate_my_attacked_icebergs(attacked_icebergs, game):
    icebergs_to_be_defended = []
    for iceberg in attacked_icebergs:
        attackers = 0
        last_attacker_arrival = 0
        for penguin_group in game.get_enemy_penguin_groups():
            if penguin_group.destination == iceberg:
                attackers += penguin_group.penguin_amount
                if penguin_group.turns_till_arrival > last_attacker_arrival:
                    last_attacker_arrival = penguin_group.turns_till_arrival

        if attackers > iceberg.penguin_amount + last_attacker_arrival * iceberg.penguins_per_turn:
            iceberg_rating = rate_iceberg(iceberg, game)
            if iceberg_rating > 20:
                icebergs_to_be_defended.append(icebergs_to_be_defended)
