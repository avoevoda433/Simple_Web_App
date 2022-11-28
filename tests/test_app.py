import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self) -> None:
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_c2f(self):
        response = self.app.get('/c2f/4.3')
        self.assertEqual(response.status_code, 200)

    def test_f2c(self):
        response = self.app.get('/f2c/4.3')
        self.assertEqual(response.status_code, 200)

    def test_warning(self):
        response = self.app.get('/warning/warning_message')
        self.assertEqual(response.status_code, 200)

    def test_convert_mode(self):
        response_c2f = self.app.get('/convert/', query_string={'direction': 'c2f', 'input_value': '5.0'})
        self.assertEqual(response_c2f.status_code, 302)
        self.assertEqual(response_c2f.location, 'http://localhost/c2f/41.0')

        response_f2c = self.app.get('/convert/', query_string={'direction': 'f2c', 'input_value': '41.0'})
        self.assertEqual(response_f2c.status_code, 302)
        self.assertEqual(response_f2c.location, 'http://localhost/f2c/5.0')

        warning_response1 = self.app.get('/convert/', query_string={'direction': 'c2f', 'input_value': ''})
        self.assertEqual(warning_response1.status_code, 302)

        warning_response2 = self.app.get('/convert/', query_string={'direction': None, 'input_value': '34.3'})
        self.assertEqual(warning_response2.status_code, 302)

        bad_response1 = self.app.get('/convert/', query_string={'direction': 'f2c', 'input_value': 'text'})
        self.assertEqual(bad_response1.status_code, 400)

    def test_not_found(self):
        response = self.app.get('/non_existent_endpoint')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
