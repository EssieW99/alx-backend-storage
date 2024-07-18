#!/usr/bin/env python3
""" a Cache class """

import redis
from typing import Union
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
