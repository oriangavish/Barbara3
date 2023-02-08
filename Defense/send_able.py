from penguin_game import *


def send_able_defense(from_iceberg, to_iceberg, penguin_group):
    if to_iceberg.get_turns_till_arrival() < penguin_group.turns_till_arrival:
        amount_needed = penguin_group.penguin_amount - (
                from_iceberg.penguin_amount + from_iceberg.penguins_per_turn * penguin_group.turns_till_arrival)
        if amount_needed < to_iceberg.penguin_amount:
            to_iceberg.send_help(amount_needed)
        else:
            return False
    else:
        amount_needed = penguin_group.penguin_amount - from_iceberg.penguin_amount + from_iceberg.penguins_per_turn * (
                to_iceberg.get_turns_till_arrival() - penguin_group.turns_till_arrival)
        if amount_needed < to_iceberg.penguin_amount:
            to_iceberg.send_help(amount_needed)
            return True
        return False
