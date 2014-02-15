from .account import CoinbaseAccount
from .account import Address
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

	def test_get_receive_address(self):
		account = CoinbaseAccount(self.authenticator)

		urllib2.urlopen = Mock(return_value=MockReader("""{"success": true,"address": "muVu2JZo8PbewBHRp6bpqFvVD87qvqEHWA","callback_url": null}"""))

		address = account.get_receive_address()

		self.assertIsInstance(address, Address)
		self.assertEquals(address.success, True)
		self.assertEquals(address.address, 'muVu2JZo8PbewBHRp6bpqFvVD87qvqEHWA')
		self.assertEquals(address.callback_url, None)

if __name__ == '__main__':
	unittest.main()