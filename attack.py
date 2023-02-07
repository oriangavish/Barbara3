from penguin_game import *
from who_should_attack import who_should_attack

# Function that sends the attack after it is already decided which iceberg to attack
def attack(game, attack_iceberg):
    attacking_icebergs = who_should_attack(game, attack_iceberg)
    for iceberg in attacking_icebergs:
        number_attack_iceberg = send_number(iceberg, attack_iceberg)
        if iceberg.can_send_penguins(attack_iceberg, number_attack_iceberg):
            iceberg.send_penguins(attack_iceberg, number_attack_iceberg)

# Again, we might want to add more penguins to the attack because they'll defend as well
def send_number(iceberg, attack_iceberg):
    number_attack_iceberg = attack_iceberg.penguin_amount
    distance = iceberg.get_turns_till_arrival(attack_iceberg)
    return number_attack_iceberg + (attack_iceberg.penguins_per_turn * distance) + 1
