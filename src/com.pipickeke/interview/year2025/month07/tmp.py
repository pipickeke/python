import time
from functools import lru_cache

def cache_with_ttl(ttl=60):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            now = time.time()
            key = args
            if key in cache:
                value, timestamp = cache[key]
                if now - timestamp < ttl:
                    return value
            result = func(*args)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

@cache_with_ttl(ttl=2)
def expensive_operation(x: int) -> int:
    return x + 1

if __name__ == "__main__":
    print(f"1: {expensive_operation(2)}")  # First call - computes
    print(f"2: {expensive_operation(2)}")  # Uses cache
    print(f"3: {expensive_operation(2)}")  # Uses cache
    time.sleep(3)  # Wait longer than TTL
    print(f"4: {expensive_operation(2)}")  # Cache expired - computes again