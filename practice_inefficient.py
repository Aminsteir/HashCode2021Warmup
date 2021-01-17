import os
from utils import Pizza,  Submission


def setup():
    for filename in os.listdir('./inputs/'):
        if filename == 'tmp':
            continue
        with open('./inputs/{}'.format(filename), 'r') as file:
            main(filename, file.readlines())


def main(e, lines):
    line_ctr = 0
    pz_avail, twos, threes, fours = [int(x) for x in lines[line_ctr].strip().split()]
    pizzas = []
    line_ctr += 1
    for i in range(pz_avail):
        ingredients = lines[line_ctr].split()[1:]
        line_ctr += 1
        pizzas.append(Pizza(i, ingredients))

    pizzas = sorted(pizzas, key=lambda d: d.ingredients, reverse=True)

    best_sub = Submission([[]])

    brute = False
    t = 1
    if brute:
        t = twos + threes + fours

    for o in range(t):
        p = o
        pz_tmp = pz_avail
        i = 4
        teams = []
        used_p = []
        u = 0
        while i >= 2:
            k = twos
            if i == 4:
                k = fours
            elif i == 3:
                k = threes

            if k - p + u < 1:
                p = o - 1
                u += 1
                i -= 1
                continue

            for t in range(k - p):
                if pz_tmp < i:
                    break
                selected_pizza = []
                for n in pizzas:
                    if len(selected_pizza) >= i:
                        break
                    if n in used_p:
                        continue
                    selected_pizza.append(n)
                    used_p.append(n)
                pz_tmp -= i
                teams.append(selected_pizza)

            i -= 1
            p = 0

        submission = Submission(teams)
        if best_sub.score < submission.score:
            best_sub = submission

    print(best_sub.score)

    f_out = open('./outputs/{}.out'.format(e), 'w')
    f_out.write(str(len(best_sub.teams)) + '\n')
    for team in best_sub.teams:
        f_out.write('{} {}\n'.format(len(team), ' '.join([str(x.id) for x in team])))


if __name__ == '__main__':
    setup()
