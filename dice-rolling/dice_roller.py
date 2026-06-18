import random
from dataclasses import dataclass, field


@dataclass
class GameState:
    dice: list = field(default_factory=list)
    rerolls_left: int = 2


def init_state():
    return GameState(dice=[random.randint(1, 6) for _ in range(5)])

def reroll(state, indices):
    if not indices:
        raise ValueError("No dice selected for rerolling")
    if state.rerolls_left <= 0:
        raise ValueError("No rerolls left")
    for i in indices:
        state.dice[i] = random.randint(1, 6)
    state.rerolls_left -= 1
