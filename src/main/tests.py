from django.test import TestCase
from django.db import IntegrityError

import datetime

from main.models.dinner import Dinner, order_dinner_by_date, sort_dinners_by_labels
from main.models.label import create_label_db
from main.models.plan import Plan, get_plans_for_date, get_plans_after_date
from main.models.date import Date


class MealTestCase(TestCase):
    def setUp(self):
        Dinner.objects.create(name="1")
        Dinner.objects.create(name="2")
        Dinner.objects.create(name="3")
        Dinner.objects.create(name="4")

    def test_latest_date(self):
        food = Dinner.objects.get(name="1")

        food.add_date(2019, 10, 1)
        food.add_date(2019, 11, 1)
        food.add_date(2019, 10, 3)

        expected = datetime.date(2019, 11, 1)
        actual = food.latest_date
        self.assertEqual(actual, expected)

    def test_order_meals(self):
        f1 = Dinner.objects.get(name="1")
        f2 = Dinner.objects.get(name="2")
        f3 = Dinner.objects.get(name="3")

        f1.add_date(2019, 12, 1)
        f2.add_date(2019, 10, 1)
        f3.add_date(2019, 11, 1)

        meals=order_dinner_by_date()

        self.assertEqual(meals[0].name, "4")
        self.assertEqual(meals[1].name, "2")
        self.assertEqual(meals[2].name, "3")
        self.assertEqual(meals[3].name, "1")

    def test_times_eaten(self):
        f1 = Dinner.objects.get(name="1")

        self.assertTrue(f1.add_date(2019, 12, 1))
        self.assertEqual(f1.times_eaten(), 1)
        self.assertTrue(f1.add_date(2019, 10, 1))
        self.assertEqual(f1.times_eaten(), 2)
        self.assertTrue(f1.add_date(2019, 11, 1))

        self.assertEqual(f1.times_eaten(), 3)

        self.assertFalse(f1.add_date(2019, 11, 1))
        self.assertEqual(f1.times_eaten(), 3)

    def test_sort_by_labels(self):
        f1 = Dinner.objects.get(name="1")
        f2 = Dinner.objects.get(name="2")
        f3 = Dinner.objects.get(name="3")
        f4 = Dinner.objects.get(name="4")

        l1 = create_label_db("simple", 1, 2, 4)
        l2 = create_label_db("fancy", 2, 4, 6)
        l3 = create_label_db("meat", 10, 16, 20)
        l4 = create_label_db("hidden", 12, 14, 22)

        f1.add_label(l1)
        f1.add_label(l2)
        f1.add_label(l3)

        f2.add_label(l2)
        f2.add_label(l4)

        f3.add_label(l1)
        f3.add_label(l2)

        f4.add_label(l2)
        f4.add_label(l3)
        f4.add_label(l4)

        sorted_1 = sort_dinners_by_labels(required=[l1, l2])
        self.assertEqual(2, len(sorted_1))
        self.assertTrue(sorted_1.filter(name='1').exists())
        self.assertTrue(sorted_1.filter(name='3').exists())

        sorted_2 = sort_dinners_by_labels(required=[l3], excluded=[l4])
        self.assertEqual(1, len(sorted_2))
        self.assertTrue(sorted_2.filter(name='1').exists())

        self.assertFalse(f2.have_label(l1))
        self.assertTrue(f2.have_label(l2))
        self.assertFalse(f2.have_label(l3))
        self.assertTrue(f2.have_label(l4))
        
        self.assertEqual(len(f1.labels.all()), 3)
        f1.add_label(l1)
        self.assertEqual(len(f1.labels.all()), 3)

    def test_label_unique(self):
        create_label_db("simple", 1, 2, 4)
        with self.assertRaises(IntegrityError) as context:
            create_label_db("simple", 6, 6, 6)

    def test_remove_label(self):
        f1 = Dinner.objects.get(name="1")

        l1 = create_label_db("simple", 1, 2, 4)
        l2 = create_label_db("fancy", 2, 4, 6)
        l3 = create_label_db("meat", 10, 16, 20)

        f1.add_label(l1)
        f1.add_label(l2)
        f1.add_label(l3)

        self.assertEqual(len(f1.labels.all()), 3)
        self.assertTrue(f1.have_label(l1))
        self.assertTrue(f1.have_label(l2))
        self.assertTrue(f1.have_label(l3))

        f1.remove_label(l2)
        f1.remove_label(l1)
        self.assertEqual(len(f1.labels.all()), 1)
        self.assertFalse(f1.have_label(l1))
        self.assertFalse(f1.have_label(l2))
        self.assertTrue(f1.have_label(l3))

    def test_get_plans(self):
        d1 = Date.objects.create(date=datetime.date(2020, 3, 1))
        d2 = Date.objects.create(date=datetime.date(2020, 2, 1))
        d3 = Date.objects.create(date=datetime.date(2020, 4, 3))
        d4 = Date.objects.create(date=datetime.date(2020, 4, 16))
        d5 = Date.objects.create(date=datetime.date(2020, 2, 1))
        Plan.objects.create(date=d1, text='d1')
        Plan.objects.create(date=d2, text='d2')
        Plan.objects.create(date=d3, text='d3')
        Plan.objects.create(date=d4, text='d4')
        Plan.objects.create(date=d5, text='d5')

        p1 = get_plans_for_date(2020, 3, 1)
        self.assertEqual(len(p1), 1)
        self.assertEqual(p1[0].text, 'd1')

        p2 = get_plans_for_date(2020, 2, 1)
        self.assertEqual(len(p2), 2)
        self.assertEqual(p2[0].text, 'd2')
        self.assertEqual(p2[1].text, 'd5')

        p3 = get_plans_for_date(2020, 4, 3)
        self.assertEqual(len(p3), 1)
        self.assertEqual(p3[0].text, 'd3')

        p4 = get_plans_for_date(2020, 4, 16)
        self.assertEqual(len(p4), 1)
        self.assertEqual(p4[0].text, 'd4')

        p5 = get_plans_after_date(2020, 3, 1)
        self.assertEqual(len(p5), 3)
        texts = {d.text for d in p5}
        self.assertSetEqual(texts, {'d1', 'd3', 'd4'})

