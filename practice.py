import os
import random
import time

from utils import Pizza, Submission, get_score, time_convert


def main(filename, lines):
    line_ctr = 0
    pz_avail, twos, threes, fours = [int(x) for x in lines[line_ctr].strip().split()]
    pizzas = []
    line_ctr += 1
    for i in range(pz_avail):
        ingredients = lines[line_ctr].split()[1:]
        line_ctr += 1
        pizzas.append(Pizza(i, ingredients, sorted_ing=False))

    # pizzas = sorted(pizzas, key=lambda d: d.ingredients, reverse=True)

    all_pz = 2 * twos + 3 * threes + 4 * fours

    trials = int(input('Number of trials: '))

    n_4 = fours
    n_3 = threes
    n_2 = twos
    total = n_4 + n_3 + n_2

    if all_pz > pz_avail:
        n_4 = min(int(pz_avail / 4) if pz_avail % 4 != 1 else int(pz_avail / 4) - 1, fours)
        r = pz_avail - n_4 * 4
        n_3 = min(int(r / 3), threes)
        r = r - n_3 * 3
        n_2 = min(int(r / 2), twos)
        total = n_4 + n_3 + n_2

    chooses = pizzas.copy()
    teams = []
    for j in range(total):
        b = 4
        if j >= n_4:
            b = 3
        if j >= n_4 + n_3:
            b = 2
        best = []
        best_choose = chooses.copy()
        for i in range(trials):
            choose_left = chooses.copy()
            selected = []
            for n in range(b):
                selected.append(choose_left[0])
                choose_left.remove(choose_left[0])
                random.shuffle(choose_left)
            if get_score([best]) < get_score([selected]):
                best = selected
                best_choose = choose_left
        chooses = best_choose
        teams.append(best)

    best = Submission(teams)

    print(best.score)

    f_out = open('./outputs/{}.out'.format(filename), 'w')
    f_out.write(str(len(best.teams)) + '\n')
    for team in best.teams:
        f_out.write('{} {}\n'.format(len(team), ' '.join([str(x.id) for x in team])))


def setup():
    for filename in os.listdir('./inputs/'):
        if filename == 'tmp':
            continue
        with open('./inputs/{}'.format(filename), 'r') as file:
            start = time.time()
            main(filename, file.readlines())
            print('{} took {}'.format(filename, time_convert(time.time() - start)))


if __name__ == '__main__':
    setup()
