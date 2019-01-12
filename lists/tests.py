from django.test import TestCase

class SmoeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

