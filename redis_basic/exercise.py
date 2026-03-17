#!/usr/bin/env python3
"""Redis basic tapşırığı: Cache klassı və store metodu"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self) -> None:
        """Redis connection qurur"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """verilenleri yaddasda saxlayir ve qaytarir"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
