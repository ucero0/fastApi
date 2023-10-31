import unittest
from core.config import Settings

class TestSettings(unittest.TestCase):
    def setUp(self):
        self.settings = Settings()
    def test_model_config(self):
        self.assertEqual(self.settings.model_config.env_file, '.env')
        self.assertEqual(self.settings.model_config.env_file_encoding, 'utf-8')


if __name__ == '__main__':
    unittest.main()