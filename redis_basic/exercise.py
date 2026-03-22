#!/usr/bin/env python3
"""Redis basic module"""
import redis
import uuid
from typing import Optional, Union


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

    def get(self, key: str,fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Redis-dən məlumatı götürür və əgər 'fn' funksiyası verilibsə, məlumatı həmin funksiya ilə çevirib qaytarır."""
        data = self._redis.get(key)
        
        if data is None:
            return None
        
        if fn:
            return fn(data)
        
        return data

    def get_str(self, key: str) -> Optional[str]:
        """converts data into string"""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """converts data to integer"""
        return self.get(key, fn=int)