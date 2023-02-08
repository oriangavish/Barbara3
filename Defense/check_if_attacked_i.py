
def check_if_attacked_i(iceberg, game):

# returns True if iceberg attacked and False if not

  for enemy in game.get_enemy_penguin_groups():
    if enemy.destination == iceberg:
      return True
    else:
      return False
