import time


class RateLimter_2:
    def __init__(self,max_request, per_second):
        self.max_request = max_request
        self.per_second = per_second
        self.timestamp = []

    def is_allow(self):
        now = time.time()

        while self.timestamp and now - self.timestamp[0] >= self.per_second:
            self.timestamp.pop()

        if len(self.timestamp) < self.max_request:
            self.timestamp.append(now)
            return True
        else:
            return False

if __name__ == '__main__':
    ratelimiter = RateLimter_2(max_request=3,per_second=1)
    assert ratelimiter.is_allow(),'限制-1'
    assert ratelimiter.is_allow(),'限制-2'
    assert ratelimiter.is_allow(),'限制-3'
    assert ratelimiter.is_allow(),'限制-4'
    assert ratelimiter.is_allow(),'限制-5'
    assert ratelimiter.is_allow(),'限制-6'
    assert ratelimiter.is_allow(),'限制-7'
