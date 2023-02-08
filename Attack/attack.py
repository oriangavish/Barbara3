from penguin_game import *
from who_should_attack import *


# Function that sends the attack after it is already decided which iceberg to attack

def attack_iceberg(game, iceberg_to_attack):
    attacking_icebergs = who_should_attack_iceberg(game, iceberg_to_attack)
    if attacking_icebergs is None:
        return False

    # If there are multiple icebergs that should attack,
    # than the who_should_attack function will return a list and an attack is done from each iceberg
    if type(attacking_icebergs) == list:
        for iceberg in attacking_icebergs:
            number_attack_iceberg = send_number(iceberg, iceberg_to_attack)
            if iceberg.can_send_penguins(iceberg_to_attack, number_attack_iceberg):
                iceberg.send_penguins(iceberg_to_attack, number_attack_iceberg)
        return True
    else:
        number_attack_iceberg = send_number(attacking_icebergs, iceberg_to_attack)
        if attacking_icebergs.can_send_penguins(iceberg_to_attack, number_attack_iceberg):
            attacking_icebergs.send_penguins(iceberg_to_attack, number_attack_iceberg)
        return True


def attack_capital(game):
    attacking_icebergs = who_should_attack_capital(game)
    for iceberg in attacking_icebergs:
        number_attack_iceberg = send_number(iceberg, game.get_enemy_icebergs()[0])
        if iceberg.can_send_penguins(attack_iceberg, number_attack_iceberg):
            iceberg.send_penguins(attack_iceberg, number_attack_iceberg)


# Again, we might want to add more penguins to the attack because they'll defend as well
def send_number(iceberg, attack_iceberg):
    number_attack_iceberg = attack_iceberg.penguin_amount
    distance = iceberg.get_turns_till_arrival(attack_iceberg)
    return number_attack_iceberg + (attack_iceberg.penguins_per_turn * distance) + 1
