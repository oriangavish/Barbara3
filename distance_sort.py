from penguin_game import *

# Function calculates the distance from the iceberg we want to defend. Our icebergs are positive numbers and the enemy icebergs are negative numbers. Netural icebergs are not included because we don't have to defend the iceberg from netural icebergs.
def distance_sort_d(game, defended_iceberg):
    all_distances = []
    all_icebergs = game.get_all_icebergs
    all_icebergs.remove(defended_iceberg)
    for iceberg in all_icebergs:
        distance = iceberg.get_turns_till_arrival(defended_iceberg)
        if iceberg in game.get_all_enemy_icebergs:
            distance *= -1
            all_distances.append([distance, iceberg])
        if iceberg in game.get_all_my_icebergs:
            all_distances.append([distance, iceberg])
    sorted_distances = all_distances.sort()
    sorted_icebergs = []
    for sorted_distance in sorted_distances:
        sorted_icebergs.append(sorted_distance[1])
    return sorted_icebergs

# Function calculates the distance from the iceberg we want want to attack from to the various options that we can attack. Here, netural icebergs are negative numbers and enemy icebergs are positive numbers. Our icebergs are not included because we can't attack our own icebergs.
def distance_sort_a(game, iceberg_attack_from):
    all_distances = []
    all_icebergs = game.get_all_icebergs
    all_icebergs.remove(iceberg_attack_from)
    for iceberg in all_icebergs:
        distance = iceberg.get_turns_till_arrival(iceberg_attack_from)
        if iceberg in game.get_all_enemy_icebergs:
            all_distances.append([distance, iceberg])
        if iceberg in game.get_netural_icebergs:
            distance *= -1
            all_distances.append([distance, iceberg])
    sorted_distances = all_distances.sort()
    sorted_icebergs = []
    for sorted_distance in sorted_distances:
        sorted_icebergs.append(sorted_distance[1])
    return sorted_icebergs

        