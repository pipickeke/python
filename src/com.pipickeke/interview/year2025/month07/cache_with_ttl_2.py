import time


def cache_with_ttl(ttl=60):
    def decorator(func):
        cache = {}

        def wrapper(*args):
            now = time.time()
            key = args
            if key in cache:
                value,timestamp = cache[key]
                if now - timestamp < ttl:
                    return value
            result = func(*args)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator


@cache_with_ttl(ttl=2)
def expensive_test(x):
    print(f"执行...")
    return x+1


if __name__ == '__main__':
    print(f"1- {expensive_test(1)}")
    print(f"2- {expensive_test(1)}")
    print(f"3- {expensive_test(1)}")
    print(f"4- {expensive_test(1)}")
    print(f"5- {expensive_test(1)}")
    print(f"6- {expensive_test(1)}")



