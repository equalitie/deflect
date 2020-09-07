from django.test import TestCase

class InitTestCase(TestCase):

    def setUp(self):
        pass

    def test_init(self):
        self.assertEqual(1, 1)
