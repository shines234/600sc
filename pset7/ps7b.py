import random
def yahtzee_monte_carlo(num_trials):
    yahtzees = 0
    for trial in range(num_trials):
        die = []
        for dice in range(5):
            die.append(random.randrange(1, 7))

        if is_yahtzee(die):
            yahtzees += 1
            print(die)
    return yahtzees/float(num_trials)


def is_yahtzee(die):
    for dice in die:
        if dice != 6:
            return False
    return True

if __name__ == '__main__':
    print(yahtzee_monte_carlo(1000000))