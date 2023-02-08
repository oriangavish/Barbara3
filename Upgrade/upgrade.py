from penguin_game import *
from should_upgrade import should_upgrade
from Ratings.rate_my_icebergs import rate_for_upgrade

def upgrade(game):
    if should_upgrade(game):
        iceberg = rate_for_upgrade(game)
        if iceberg.upgrade_cost < iceberg.penguin_amount and iceberg.can_upgrade():
            iceberg.upgrade()

