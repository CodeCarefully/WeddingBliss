from django.test import TestCase

# Create your tests here.


class TestTests(TestCase):

    def test_example(self):
        """
        test comment
        """
        self.assertIs("bye","hi")