import unittest

from dishes import Dish, choose_best_dish_for_dinner


# Sample Dishes for testing - the pasta_with_pesto and pasta_with_truffels dishes have one keyword 
# in common 'pasta'
pasta_with_pesto = Dish(
    name="Pasta con Pesto al Gevonese",
    flavour=8.30,
    ingredients=["pasta", "pesto", "cheese", "olive_oil"],
)

pasta_with_truffels = Dish(
    name="Pasta con Truffels",
    flavour=9.10,
    ingredients=["pasta", "truffels", "souce_cream", "garlic", "ruccola"],
)

steak_tomahawk = Dish(
    name="Steak Tomahawk",
    flavour=9.50,
    ingredients=["meat", "pepper", ],
)


class ReceiptTest(unittest.TestCase):

    def test_it_picks_no_dish_if_no_ingridient_match(self):
        chosen_receipt = choose_best_dish_for_dinner(
            disired_ingredients=["fish"],
            dishes=[steak_tomahawk],
        )
        self.assertIsNone(chosen_receipt)

    def test_it_chooses_a_dish_if_ingridient_match_keywords(self):
        chosen_receipt = choose_best_dish_for_dinner(
            disired_ingredients=["meat"],
            dishes=[steak_tomahawk],
        )
        self.assertEqual(steak_tomahawk, chosen_receipt)

    def test_it_chooses_dish_with_most_overlapping_ingridients(self):

        # TODO: tests covering remaining functionality


if __name__ == '__main__':
    unittest.main()
