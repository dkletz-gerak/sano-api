import json
from core.redis.redis import RedisClient


# Yeah, two type of data => dict (obj) or string
# Default dict
class RedisBaseModel:
    def __init__(self, key):
        self._key = key
        self._r = RedisClient.load()
        self._fields = []
        self.__expiry = None
        self._is_data_object = True
        self._data = None

    def _set_expiry(self, expiry: int):
        self.__expiry = expiry

    def _set_data(self, data):
        if self._is_data_object:
            self._set_data_object(data)
        else:
            self._data = data

    def _set_data_object(self, data):
        if self._data is None:
            self._data = {}

        for key, val in data.items():
            if key in self._fields:
                self._data[key] = val
            else:
                raise Exception("Incomplete fields")

    def save(self):
        serializable = self._data
        serialized = json.dumps(serializable)

        return self._r.set(
            self._key + "_" + type(self).__name__, serialized, self.__expiry
        )

    def load(self):
        data = self._r.get(self._key + "_" + type(self).__name__)

        if data is None:
            return None

        data = json.loads(data)
        self._set_data(data)
        return self.data

    def delete(self):
        self._r.delete(self._key + "_" + type(self).__name__)

    # Deprecated since we now save in _data?
    # Gab will need decide later
    def to_dict(self):
        data = {}

        for field_name in self._fields:
            data[field_name] = getattr(self, field_name)

        return data

    @property
    def data(self):
        return self._data
