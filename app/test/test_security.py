# FILEPATH: /b:/Python projects/fastApi/app/test/test_security.py

import unittest
from core.security import get_password_hash

class TestSecurity(unittest.TestCase):
    def test_get_password_hash(self):
        # Test if the function returns a string
        self.assertIsInstance(get_password_hash('password'), str)

        # Test if the function returns a different hash for different passwords
        password1 = 'password1'
        password2 = 'password2'
        hash1 = get_password_hash(password1)
        hash2 = get_password_hash(password2)
        self.assertNotEqual(hash1, hash2)

        # Test if the function returns the same hash for the same password
        hash3 = get_password_hash(password1)
        self.assertEqual(hash1, hash3)

if __name__ == '__main__':
    unittest.main()