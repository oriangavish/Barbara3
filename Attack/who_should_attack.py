from penguin_game import *


def calculateDistance(my_iceberg, attack_iceberg):
    return my_iceberg.get_turns_till_arrival(attack_iceberg)


# We might want to make there need to be a certain
# amount of penguins sent during the attack in case they defend their iceberg
def who_should_attack(game, attack_iceberg):
    icebergs = game.get_my_icebergs
    icebergs_by_distance = []
    distances = []
    for iceberg in icebergs:
        distance = calculateDistance(iceberg, attack_iceberg)
        distances.append(distance)
        icebergs_by_distance.append([distance, iceberg])
    icebergs_by_distance.sort()
    for iceberg in icebergs_by_distance:
        distance = iceberg[0]
        if attack_iceberg.penguin_amount + (distance * attack_iceberg.penguins_per_turn) < iceberg[1].penguin_amount:
            return iceberg[1]
    # Multiple icebergs of the same distance from enemy iceberg
    for distance in distances:
        if distances.count(distance) > 1:
            icebergs_to_attack = check_multiple_hits(distance, icebergs_by_distance, attack_iceberg)
            if icebergs_to_attack is not None:
                return icebergs_to_attack
    return None


# If there are multiple icebergs in the same distances, we can send penguins from both at
# the same time if it's not possible to send penguins from only one and still be able to attack the enemy iceberg
def check_multiple_hits(distance, icebergs_by_distance, attack_iceberg):
    same_distance_icebergs = []
    total_penguin_count = 0
    for iceberg in icebergs_by_distance:
        if iceberg[0] == distance:
            total_penguin_count += iceberg[1].penguin_amount
            same_distance_icebergs.append(iceberg[1])
    if attack_iceberg.penguin_amount + (distance * attack_iceberg.penguins_per_turn) < total_penguin_count:
        return same_distance_icebergs
    return None
