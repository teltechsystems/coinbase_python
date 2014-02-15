class Button(object):
    __slots__ = [
        'name', 'custom', 'callback_url', 'description', 'type', 'style', 'include_email', 
        'text', 'code', 'price'
    ]

    def __init__(self, name, **optional_kwargs):
        self.name = name

        for k, v in optional_kwargs.items():
            setattr(self, k, v)

        if not optional_kwargs.get('type'):
            self.type = 'buy_now'

        if not optional_kwargs.get('style'):
            self.style = 'buy_now_large'

        if not optional_kwargs.get('text'):
            self.text = 'Pay With Bitcoin'