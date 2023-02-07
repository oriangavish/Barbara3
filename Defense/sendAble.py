from penguin_game import *


def send_able(self, iceberg, penguin_group):
    if iceberg.get_turns_till_arrival() < penguin_group.turns_till_arrival:
        amount_needed = penguin_group.penguin_amount - (
                    self.penguin_amount + penguins_per_turn * penguin_group.turns_till_arrival)
        if amount_needed < iceberg.penguin_amount:
            iceberg.send_help(amount_needed)
        else:
            return False
    else:
        amount_needed = penguin_group.penguin_amount - self.penguin_amount + penguins_per_turn * (
                    iceberg.get_turns_till_arrival() - penguin_group.turns_till_arrival)
        if amount_needed < iceberg.penguin_amount:
            iceberg.send_help(amount_needed)
            return True
        return False
