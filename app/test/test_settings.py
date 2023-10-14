import unittest
from ..core.config import settings

class TestSettings(unittest.TestCase):
    def test_model_config(self):
        self.assertEqual(settings.model_config.env_file, '.env')
        self.assertEqual(settings.model_config.env_file_encoding, 'utf-8')


if __name__ == '__main__':
    unittest.main()