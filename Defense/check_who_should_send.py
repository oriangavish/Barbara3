from penguin_game import *
from send_able import send_able_defense


# Function returns list of surrounding icebergs that should send help.
# If needed it should ask for help from all our icebergs.
def check_who_should_send_to_capital(game, penguin_group):
    my_icebergs = game.get_my_icebergs()
    amount_acquired = 0
    counter = 0
    while True:
        sent = send_able_defense(my_icebergs[counter], penguin_group)
        if sent:
            break
        else:
            counter += 1


# Function returns list of surrounding icebergs that should send help. Maximum helpers should be 2 for now.
# We can change later if needed.
def check_who_should_send_to_iceberg(iceberg_to_defend):
    return
