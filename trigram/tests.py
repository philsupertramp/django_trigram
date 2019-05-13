import random

from parameterized import parameterized
from django.test import TestCase

from trigram.models import ModelA, ModelB, ModelC


class TrigramTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        titles = [
            'Co-Founder /Entrepreneur in Residence - Marketing and Business Development (m/f/x)',
            'Developer Embedded Hardware / Software (m/w/d)',
            'EMBEDDED SOFTWARE ENGINEER (m/f)',
            'Chief Technology Officer (F/M/DIV)'
        ]
        names = [
            ('Adam', 'Zelcher'),
            ('Ben', 'Yelcher'),
            ('Cansas', 'Xelcher'),
            ('Dan', 'Welcher'),
            ('Tina', 'Velcher'),
        ]

        ModelA.objects.bulk_create([
            ModelA(title=i) for i in titles
        ])
        ModelB.objects.bulk_create([
            ModelB(first_name=i, last_name=j) for (i, j) in names
        ])
        ModelC.objects.bulk_create([
            ModelC(b=ModelB.objects.get(pk=random.randint(1, len(names))), a=i) for i in ModelA.objects.all()
        ])

    @parameterized.expand([
        ('Ben', 1),
        ('Belcher', 4),
        ('CTO', 2),
        ('Software', 2)
    ])
    def test_trigram_stuff(self, search_val, expected_count):
        qs = ModelC.objects.search(search_val)
        num_results = qs.count()
        self.assertEqual(expected_count, num_results)
