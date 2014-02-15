from .auth import Authenticator
from .client import do_request

class Balance(object):
	__slots__ = ['amount', 'currency']

	def __init__(self, amount, currency):
		self.amount = float(amount)
		self.currency = currency

	def __str__(self):
		return '%.8f %s' % (self.amount, self.currency, )

class Address(object):
	__slots__ = ['address', 'callback_url', 'label']

	def __init__(self, address, callback_url, label = ''):
		self.address = address
		self.callback_url = callback_url
		self.label = label

class CoinbaseAccount(object):
	def __init__(self, authenticator):
		assert isinstance(authenticator, Authenticator)

		self.authenticator = authenticator

	def get_addresses(self):
		paged_response = do_request(self.authenticator, 'GET', '/addresses')

		addresses = []

		for json_address in paged_response['addresses']:
			addresses.append(Address(json_address['address']['address'], json_address['address']['callback_url'], json_address['address']['label']))

		return addresses

	def get_balance(self):
		json_balance = do_request(self.authenticator, 'GET', '/account/balance')

		return Balance(json_balance['amount'], json_balance['currency'])

	def get_receive_address(self):
		json_address = do_request(self.authenticator, 'GET', '/account/receive_address')

		return Address(json_address['address'], json_address['callback_url'])