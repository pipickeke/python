import time


class RateLimiter:
    def __init__(self, max_requests, per_second):
        self.max_requests = max_requests
        self.per_second = per_second
        self.timestamp = []

    def is_allow(self):
        now = time.time()

        while self.timestamp and now - self.timestamp[0] >= self.per_second:
            self.timestamp.pop(0)

        if len(self.timestamp) < self.max_requests:
            self.timestamp.append(now)
            return True
        else:
            return False


if __name__ == '__main__':
    # 1，测试基础功能
    limiter = RateLimiter(max_requests=2, per_second=1)
    assert limiter.is_allow() == True,'限制'
    assert limiter.is_allow() == True,''
    assert limiter.is_allow() == True,'限制'





