from django.test import TestCase

from datetime import date

from main.models import Meal


class MealTestCase(TestCase):
    def setUp(self):
        Meal.objects.create(name="Food")

    def test_latest_date(self):
        food = Meal.objects.get(name="Food")

        food.add_date(2019, 10, 1)
        food.add_date(2019, 11, 1)
        food.add_date(2019, 10, 3)

        expected = date(2019, 11, 1)
        actual = food.latest_date()
        self.assertEqual(actual, expected)

