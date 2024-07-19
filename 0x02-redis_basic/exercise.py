#!/usr/bin/env python3
""" a Cache class """

import redis
from typing import Callable, Optional, Union
import uuid


class Cache:
    """ a simple cache """

    def __init__(self):
        """ initialises a redis instance """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generate a random key store the input data in Redis using
        the random key and return the key
        """

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> str:
        """
        Retrieves the data associated with the key from Redis.
        Callable arg converts the data back to the desired format
        """

        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        retrieves a value from Redis and automatically decode it from bytes
        to a UTF-8 string
        """

        return self.get(key, lambda x: x.decode('utf-8', 'strict'))

    def get_int(self, key: str) -> Optional[int]:
        """
        retrieves a value from Redis and automatically decode it from bytes
        to an int
        """

        return self.get(key, lambda x: int(x))
