#!/usr/bin/env python3
"""
Redis ilə işləmək üçün Cache klassı.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Məlumatları Redis-də saxlamaq üçün keş sistemi.
    """

    def __init__(self):
        """
        Redis müştərisini (client) yaradır və verilənlər bazasını təmizləyir.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Daxil edilən məlumatı təsadüfi bir key ilə Redis-də saxlayır.

        Args:
            data: Saxlanılacaq məlumat (str, bytes, int və ya float).

        Returns:
            Generasiya olunmuş random key (string).
        """
        # Təsadüfi ID (key) yaradırıq
        random_key = str(uuid.uuid4())
        
        # Məlumatı Redis-də saxlayırıq
        self._redis.set(random_key, data)
        
        return random_key