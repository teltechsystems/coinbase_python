from .account import CoinbaseAccount
from .auth import KeySecretAuthenticator
from .client import urllib2
from mock import Mock
from .test_utils import MockReader

import unittest

class CoinbaseAccountTestCase(unittest.TestCase):
	def setUp(self):
		self.authenticator = KeySecretAuthenticator('abc', '123')

	def test_init(self):
		with self.assertRaises(AssertionError):
			CoinbaseAccount({})

		account = CoinbaseAccount(self.authenticator)

		self.assertEquals(account.authenticator, self.authenticator)

	def test_get_balance(self):
		account = CoinbaseAccount(self.authenticator)
		
		urllib2.urlopen = Mock(return_value=MockReader("""{"amount": "36.62800000", "currency": "BTC"}"""))

		balance = account.get_balance()

		self.assertEquals(str(balance), '36.62800000 BTC')
		self.assertEquals(balance.amount, 36.62800000)
		self.assertEquals(balance.currency, 'BTC')

if __name__ == '__main__':
	unittest.main()