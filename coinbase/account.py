from .auth import Authenticator
from .client import do_request

class Balance(object):
	__slots__ = ['amount', 'currency']

	def __init__(self, amount, currency):
		self.amount = float(amount)
		self.currency = currency

	def __str__(self):
		return '%.8f %s' % (self.amount, self.currency, )

class CoinbaseAccount(object):
	def __init__(self, authenticator):
		assert isinstance(authenticator, Authenticator)

		self.authenticator = authenticator

	def get_balance(self):
		json_balance = do_request(self.authenticator, 'GET', '/account/balance')

		return Balance(json_balance['amount'], json_balance['currency'])