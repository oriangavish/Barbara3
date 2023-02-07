from penguin_game import *


def rate_enemy_C(game, sorted_friendlies, sorted_enemies):
    icepitals_to_attack = []
    for i in range(2, 5):
        for icepital in game.get_enemy_icepital_icebergs():
            attacker_force = 0
            defender_force_at_arrival = 0
            for friendly in sorted_friendlies[:3]:
                if friendly.get_turns_till_arrival(icepital) <= i:
                    attacker_force += friendly.penguin_amount
            defender_force_at_arrival += icepital.penguin_amount
            defender_force_at_arrival += (icepital.penguins_per_turn * i)
            for enemy in sorted_enemies[:2]:
                defender_force_at_arrival += enemy.penguin_amount + enemy.penguins_per_turn

            if attacker_force > defender_force_at_arrival:
                icepitals_to_attack.append(icepital)

    return icepitals_to_attack

