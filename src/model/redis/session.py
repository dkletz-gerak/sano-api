from .redis_base_model import RedisBaseModel


class Session(RedisBaseModel):
    def __init__(self, key, data=None):
        super().__init__(key)
        self._fields = ["id", "email", "name", "verified", "role"]
        if data:
            self._set_data(data)
