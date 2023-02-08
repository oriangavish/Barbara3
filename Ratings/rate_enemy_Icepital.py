from penguin_game import *


def rate_enemy_C(game, sorted_friendlies, sorted_enemies):
    # FRIENDLIES MEANS OUR ICEBERGS!
    # The friendlies are sorted by their distance from enemy capital.
    # The function looks forward five turns.
    # If, in one of those iterations, an attacking force from our three closest icebergs (FRIENDLIES!) to that capital
    # will be able to overpower the defense by the time of its arrival,
    # the function will add the capital to the list of capitals that are vulnerable to be attacked.
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

