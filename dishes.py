"""
Let's build platform for finding best dish for dinner. 
"""


class Dish:
    """A reciept we can cook for dinner."""

    def __init__(self):
        """
        :param name: unique name for this receipt, e.g. "Pasta con Tommatten"
        :param value: flavour from 0 to 10 that shows how tasty dish is, e.g. 7,3. 
        :param ingredients: list of ingredients we are using to cook this dish. 
        """
        # TODO: implement constructor (you can assume parameters will always be valid)

    def __repr__(self):
        # TODO: implement human-readable string representation of dish

def choose_best_dish_for_dinner(disired_ingredients, dishes):
    """Returns the best dish for dinner for a given disired ingredients
     or None if no dish is matched. A user can choose dish if they
    have searched for at least one(!) ingredient from the dish.

    The "best" dish to serve is the one with the most ingredients
    matches.

    If two or more receipts have the same number of matches then the
    one with the highest flavour should be served.

    If two or more receipts have the same number of matches and the
    same flavour, then either one may be returned.

    :param disired_ingredients: list of ingredients. assume normalized
    :param dishes: a collection of Dish objects
    :return: A single Dish object considered the 'best' dish to show 
            for the search ingredients provided or None if no dishes
            are eligible
    """

    # TODO: implement decision logic.
    pass
    

