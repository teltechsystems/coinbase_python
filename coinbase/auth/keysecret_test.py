from .keysecret import KeySecretAuthenticator

import time
import unittest
import urllib2

class KeySecretAuthenticatorTestCase(unittest.TestCase):
	def test_init(self):
		authenticator = KeySecretAuthenticator('abc', '123')

		self.assertEquals(authenticator.api_key, 'abc')
		self.assertEquals(authenticator.api_secret, '123')

	def test_generate_signature(self):
		request = urllib2.Request(url='https://www.coinbase.com/api/v1')
		authenticator = KeySecretAuthenticator('abc', '123')

		self.assertEquals(authenticator.generate_signature(request, 1), 'daa699bcfd30ff1f4ad64092e1c766f104a6c6aeee5d4b3bcbdccb5f1b414c1c')

	def test_get_headers(self):
		authenticator = KeySecretAuthenticator('abc', '123')
		request = urllib2.Request(url='https://www.coinbase.com/api/v1')
		headers = authenticator.get_headers(request)

		self.assertEquals(headers['Content-Type'], 'application/json')
		self.assertEquals(headers['ACCESS_KEY'], 'abc')
		self.assertTrue('ACCESS_NONCE' in headers)
		self.assertEquals(headers['ACCESS_SIGNATURE'], authenticator.generate_signature(request, headers['ACCESS_NONCE']))

if __name__ == '__main__':
	unittest.main()