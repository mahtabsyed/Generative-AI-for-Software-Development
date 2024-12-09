import unittest
from flask.testing import FlaskClient
from simple_flask import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_no_query_parameter(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Greetings')

    def test_valid_query_parameter(self):
        response = self.app.get('/?name=Alice')
        self.assertEqual(response.data.decode(), 'Greetings, Alice!')

    def test_empty_query_parameter(self):
        response = self.app.get('/?name=')
        self.assertEqual(response.data.decode(), 'Greetings')

    def test_special_characters_in_query_parameter(self):
        response = self.app.get('/?name=Alice%20Smith')
        self.assertEqual(response.data.decode(), 'Greetings, Alice Smith!')

    def test_numerical_query_parameter(self):
        response = self.app.get('/?name=1234')
        self.assertEqual(response.data.decode(), 'Greetings, 1234!')

    def test_long_string_query_parameter(self):
        long_name = 'a' * 1000
        response = self.app.get(f'/?name={long_name}')
        self.assertEqual(response.data.decode(), f'Greetings, {long_name}!')

    def test_html_script_in_query_parameter(self):
        response = self.app.get('/?name=<h1>Test</h1>')
        self.assertEqual(response.data.decode(), 'Greetings, <h1>Test</h1>!')

if __name__ == '__main__':
    unittest.main()