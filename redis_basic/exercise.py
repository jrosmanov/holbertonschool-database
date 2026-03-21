#!/usr/bin/env python3
"""
This module has a Cache class with __init__ method and a private variable 
"""
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper
                
class Cache:
    """
    A class with __init__ method and a private variable
    """
    def __init__(self) -> None:
        """
        Method that initializes redis instance and flushes the db
        """
        import redis
        
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Metod that takes uuid data type and returns str
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[int, bytes, float, str, None]:
        """
        Retrieves data from redis and applies optional conversion
        """
        data = self._redis.get(key)
        if key is not None and fn is not None:
            return fn(data) 
        return data

    def get_str(self, key: str) -> str:
        """
        Converts redis bytes into string
        """
        key = self.get(key, lambda d: d.decode("utf-8"))
        return key

    def get_int(self, key: int) -> int:
        """
        Converts redis bytes into integer
        """
        key = self.get(key, int)
        return key