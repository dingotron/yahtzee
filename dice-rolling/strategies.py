from dice_roller import reroll


def sixes_strategy(state):
    while state.rerolls_left > 0:
        indices_to_reroll = [i for i, die in enumerate(state.dice) if die != 6]
        if not indices_to_reroll:
            break
        reroll(state, indices_to_reroll)
    return state.dice
