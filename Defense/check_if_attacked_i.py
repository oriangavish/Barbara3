def check_if_attacked_i(iceberg, game):
    # returns True if iceberg attacked and False if not

    for enemy in game.get_enemy_penguin_groups():
        if enemy.destination == iceberg:
            return True
        else:
            return False


def find_all_attacked_icebergs(game):
    # Checks all our icebergs to see if attacked
    attacked_icebergs = []
    for iceberg in game.get_my_icebergs():
        if check_if_attacked_i(iceberg, game):
            attacked_icebergs.append(iceberg)

    return attacked_icebergs
