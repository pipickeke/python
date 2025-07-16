from threading import Lock

class ThreadSafeSingleton:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if not isinstance(cls._instance, cls):
                cls._instance = super().__new__(cls)
        return cls._instance


