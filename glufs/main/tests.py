from django.test import TestCase

from datetime import date

from main.models import Meal, order_meal_by_date


class MealTestCase(TestCase):
    def setUp(self):
        Meal.objects.create(name="1")
        Meal.objects.create(name="2")
        Meal.objects.create(name="3")
        Meal.objects.create(name="4")

    def test_latest_date(self):
        food = Meal.objects.get(name="1")

        food.add_date(2019, 10, 1)
        food.add_date(2019, 11, 1)
        food.add_date(2019, 10, 3)

        expected = date(2019, 11, 1)
        actual = food.latest_date
        self.assertEqual(actual, expected)

    def test_order_meals(self):
        f1 = Meal.objects.get(name="1")
        f2 = Meal.objects.get(name="2")
        f3 = Meal.objects.get(name="3")

        f1.add_date(2019, 12, 1)
        f2.add_date(2019, 10, 1)
        f3.add_date(2019, 11, 1)

        meals=order_meal_by_date()

        self.assertEqual(meals[0].name, "4")
        self.assertEqual(meals[1].name, "2")
        self.assertEqual(meals[2].name, "3")
        self.assertEqual(meals[3].name, "1")

    def test_times_eaten(self):
        f1 = Meal.objects.get(name="1")

        f1.add_date(2019, 12, 1)
        self.assertEqual(f1.times_eaten(), 1)
        f1.add_date(2019, 10, 1)
        self.assertEqual(f1.times_eaten(), 2)
        f1.add_date(2019, 11, 1)

        self.assertEqual(f1.times_eaten(), 3)

        f1.add_date(2019, 11, 1)
        self.assertEqual(f1.times_eaten(), 3)
