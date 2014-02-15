from .auth import KeySecretAuthenticator
from .client import do_request, urllib2
from mock import Mock
from .test_utils import MockReader

import unittest

class ClientTestCase(unittest.TestCase):
	def test_do_request(self):
		authenticator = KeySecretAuthenticator('abc', '123')

		urllib2.urlopen = Mock(return_value=MockReader("""{"amount": "36.62800000", "currency": "BTC"}"""))

		response = do_request(authenticator, 'GET', '/account/balance')

		self.assertEquals(response['amount'], '36.62800000')
		self.assertEquals(response['currency'], 'BTC')

if __name__ == '__main__':
	unittest.main()