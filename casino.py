# no work,back to vidio  2:20

from util import flip_coin

HEADS = "heads"
TAILS = "tails"
COIN_VAL = [HEADS, TAILS]


def play_martingale(start_funds: int, min_bet: int, max_bet: int) -> int:
    steps_to_loose = 0
    current_funds = start_funds
    current_bet = min_bet

    while current_funds > 0:
        print("======")
        steps_to_loose += 1
        current_funds -= current_bet
        # print(f"{current_funds=}, {current_bet}")
        if flip_coin(COIN_VAL) == HEADS:
            win = current_funds * 2
            # print(f"{win=}")
            current_funds += win
            current_bet = min_bet
        else:
            print("loose")
            current_bet *= 2
            if current_bet > max_bet:
                current_bet = min_bet
            if current_bet > current_funds:
                current_bet = current_funds

    return current_funds

start_found = 25
print(play_martingale(start_funds=start_found, min_bet=1, max_bet=start_found - 1))


