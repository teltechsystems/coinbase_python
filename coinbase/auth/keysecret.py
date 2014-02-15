from .base import Authenticator

import hashlib
import hmac
import time

class KeySecretAuthenticator(Authenticator):
	def __init__(self, api_key, api_secret):
		self.api_key = api_key
		self.api_secret = api_secret

	def generate_signature(self, request, nonce):
		message = str(nonce) + request.get_full_url() + (request.get_data() or '')

		return hmac.new(str(self.api_secret), message, hashlib.sha256).hexdigest()

	def get_headers(self, request):
		nonce = int(time.time() * 1e6)

		return {
			'Content-type'		: 'application/json',
			'ACCESS_KEY'		: self.api_key,
			'ACCESS_NONCE'		: nonce,
			'ACCESS_SIGNATURE'	: self.generate_signature(request, nonce)
		}