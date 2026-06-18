from collections import Counter
from dice_roller import init_state
from strategies import sixes_strategy


def simulate(strategy, n=1000):
    counter = Counter()
    for _ in range(n):
        state = init_state()
        final_dice = strategy(state)
        num_sixes = sum(1 for die in final_dice if die == 6)
        counter.update([num_sixes])
    return counter


if __name__ == "__main__":
    counter = simulate(sixes_strategy)
    print("Distribution of 6s in final roll after 1000 simulations:")
    for i in range(6):
        print(f"{i} sixes: {counter[i]} times")
