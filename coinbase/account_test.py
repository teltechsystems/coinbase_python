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

	def test_get_addresses(self):
		account = CoinbaseAccount(self.authenticator)

		urllib2.urlopen = Mock(return_value=MockReader("""{
  "addresses": [
    {
      "address": {
        "address": "moLxGrqWNcnGq4A8Caq8EGP4n9GUGWanj4",
        "callback_url": null,
        "label": "My Label",
        "created_at": "2013-05-09T23:07:08-07:00"
      }
    },
    {
      "address": {
        "address": "mwigfecvyG4MZjb6R5jMbmNcs7TkzhUaCj",
        "callback_url": null,
        "label": null,
        "created_at": "2013-05-09T17:50:37-07:00"
      }
    }
  ],
  "total_count": 2,
  "num_pages": 1,
  "current_page": 1
}"""))

		addresses = account.get_addresses()

		self.assertEquals(len(addresses), 2)

		valid_addresses = ['moLxGrqWNcnGq4A8Caq8EGP4n9GUGWanj4', 'mwigfecvyG4MZjb6R5jMbmNcs7TkzhUaCj']

		for i, address in enumerate(addresses):
			self.assertEquals(address.address, valid_addresses[i])

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
		self.assertEquals(address.address, 'muVu2JZo8PbewBHRp6bpqFvVD87qvqEHWA')
		self.assertEquals(address.callback_url, None)

if __name__ == '__main__':
	unittest.main()