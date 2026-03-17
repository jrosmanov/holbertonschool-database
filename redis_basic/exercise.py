#!/usr/bin/env python3
"""Redis basic module"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        """creating redis for data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """storing data in redis"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
