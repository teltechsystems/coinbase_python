class MockReader(object):
	def __init__(self, body):
		self.body = body

	def read(self):
		return self.body