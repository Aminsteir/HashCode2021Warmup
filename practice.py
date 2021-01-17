import os
import random

from utils import Pizza, Submission, get_score


def main(filename, lines):
    line_ctr = 0
    pz_avail, twos, threes, fours = [int(x) for x in lines[line_ctr].strip().split()]
    pizzas = []
    line_ctr += 1
    for i in range(pz_avail):
        ingredients = lines[line_ctr].split()[1:]
        line_ctr += 1
        pizzas.append(Pizza(i, ingredients))

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

    best = Submission([[]])
    for i in range(trials):
        chooses = pizzas.copy()
        teams = []
        for j in range(total):
            b = 4
            if j >= n_4:
                b = 3
            if j >= n_4 + n_3:
                b = 2
            selected = []
            for n in range(b):
                selected.append(chooses[0])
                chooses.remove(chooses[0])
                random.shuffle(chooses)
            teams.append(selected)
        if get_score(teams) > best.score:
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
            main(filename, file.readlines())


if __name__ == '__main__':
    setup()
