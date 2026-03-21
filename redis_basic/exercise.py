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
    
    def get(self, key: str, fn=None) -> Union[str, bytes, int, float]:
        """getting data from redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value
    
    def get_str(self, key: str) -> str:
        """getting string data from redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        return value.decode('utf-8')
    
    def get_int(self, key: str) -> int:
        """getting integer data from redis"""
        value = self._redis.get(key)
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            return None
