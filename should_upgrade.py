from penguin_game import *
from Defense.check_if_c_safe import check_if_c_safe
# Currently the two functions below don't exist, but when it does, it needs to be included here
from Defense.check_if_safe_I import check_if_safe_I
from Defense.check_if_defended_I import check_if_defended_I

# Checks if it is worth it to upgrade one of the icebergs. If this function returns true, than the rate_for_upgrade function should be run to decide which of the icebergs should be upgraded. Here, each enemy group is checked to see whether their target can be defended or not, and whether it's worth it to upgrade while we should be defending instead. 
def should_upgrade(game):
    current_enemy_groups = game.get_enemy_penguin_groups
    non_direct_enemy_groups = []
    my_icebergs = game.get_my_icebergs
    netural_icebergs = game.get_netural_icebergs
    enemy_icebergs = game.get_enemy_icebergs
    for enemy_group in current_enemy_groups:
        enemy_group_destination = enemy_group.destination
        if enemy_group.destination.is_icepital and check_if_c_safe(current_enemy_groups) == False:
            return False
        if enemy_group.destination in my_icebergs and check_if_safe_I(enemy_group_destination) == False:
            if check_if_defended_I(enemy_group_destination) == False:
                return False
        if enemy_group_destination in netural_icebergs:
            non_direct_enemy_groups.append(enemy_group)
        if enemy_group_destination in enemy_icebergs:
            non_direct_enemy_groups.append(enemy_group)
        
    # if the function gets to here, than that means enemy_group is either heading toward a neutral place, or enemy_group is going to defend their own iceberg, or any icebergs that an enemy_group is attacking are defended and safe from being taken. If there are more than 2 groups enroute, it will return false as well because we want to make sure that enemy_group isn't defending their own icebergs or attacking a neutral iceberg without interference.
    if len(non_direct_enemy_groups) > 2:
        return False
    return True
