import camelcase
import unittest
from unittest import TestCase

class TestCamelCase(TestCase):

    # Test the camelcase function
    def test_camelcase_sentence(self):
        self.assertEqual('helloWorld', camelcase.camel_case('Hello wOrlD'))
        self.assertEqual('', camelcase.camel_case(''))
        self.assertEqual('helloWorld', camelcase.camel_case('    Hello    World     '))

    # Test the symbol filter function
    # Test to see if symbols are removed regadless of which part of string it is located
    def test_symbol_filter(self):
        self.assertEqual('HELLOWORLD', camelcase.symbol_filter('/ HELLO * WORLD -'))
        self.assertEqual('helloWorld', camelcase.symbol_filter('/ hello * World -'))


if __name__ == '__main__':
    unittest.main()