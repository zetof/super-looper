class Subscriber:

    def __init__(self, callback_class, callback_method, enabled, with_data):
        self._callback_class = callback_class
        self._callback_method = callback_method
        self._enabled = enabled
        self._with_data = with_data

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False

    def notify(self, **kwargs):
        if self._enabled:
            if kwargs and self._with_data:
                self._callback_method.__func__(self._callback_class, **kwargs)
            else:
                self._callback_method.__func__(self._callback_class)

