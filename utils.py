class Pizza(object):
    def __init__(self, p_id, ingredients, sorted_ing=True):
        self.ingredients = ingredients
        if sorted_ing:
            self.ingredients = sorted(ingredients)
        self.id = p_id
        self.n = len(ingredients)

    def __cmp__(self, other):
        return self.ingredients == other.ingredients

    def __str__(self):
        return str(self.ingredients)

    def __repr__(self):
        return str(self)


class Submission(object):
    def __init__(self, team_pizzas):
        self.score = get_score(team_pizzas)
        self.teams = team_pizzas


def get_score(teams):
    t_s = 0
    for team in teams:
        ingredients = []
        for pi in team:
            for ingredient in pi.ingredients:
                if ingredient not in ingredients:
                    ingredients.append(ingredient)
        t_s += (len(ingredients) ** 2)
    return t_s
