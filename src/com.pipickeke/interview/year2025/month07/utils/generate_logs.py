"""

生成日志：

192.168.1.10 - - [01/Jul/2025:10:15:42 +0800] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - - [01/Jul/2025:10:16:01 +0800] "POST /login HTTP/1.1" 302 512 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
172.16.5.23 - - [01/Jul/2025:10:16:15 +0800] "GET /images/logo.png HTTP/1.1" 200 2048 "-" "curl/7.29.0"
192.168.1.10 - - [01/Jul/2025:10:17:42 +0800] "GET /dashboard HTTP/1.1" 200 4096 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - - [01/Jul/2025:10:18:03 +0800] "GET /logout HTTP/1.1" 200 256 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

"""

import random
import time
import threading
import argparse

from datetime import datetime

# 模拟ip池子
def generate_ip():
    return f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"


# 模拟请求路径
paths = [
    "/index.html", "/about", "/login", "/logout", "/search", "/product?id=123",
    "/cart", "/checkout", "/api/data", "/admin"
]

# 模拟 User-Agent
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "curl/7.29.0",
    "Wget/1.20.3",
    "PostmanRuntime/7.28.0",
    "Mozilla/5.0 (Linux; Android 10; SM-G973F)"
]

status_code = [200, 301, 302, 403, 404, 500]
methods = ["GET", "POST", "PUT", "DELETE"]

# 每行生成一个标准的web 日志格式
def generate_log_line():
    ip = generate_ip()
    timestamp = datetime.now().strftime("%d/%b/%Y:%H:%M:%S +0800")
    method = random.choice(methods)
    path = random.choice(paths)
    status = random.choice(status_code)
    size = random.randint(100, 5000)
    user_agent = random.choice(user_agents)
    return f'{ip} - - [{timestamp}] "{method} {path} HTTP/1.1" {status} {size} "-" "{user_agent}"\n'


def write_thread(thread_id, lines_per_thread, output_path):
    with open(output_path, 'a') as f:
        for _ in range(lines_per_thread):
            f.write(generate_log_line())


def main():
    parser = argparse.ArgumentParser(description="Fake web log generator")
    parser.add_argument('--lines', type=int, default=100, help="Total line to generate")
    parser.add_argument('--threads', type=int, default=2, help="Number of threads")
    parser.add_argument('--output', type=str, default="access.log", help="Output file path")
    args = parser.parse_args()

    lines_per_thread = args.lines // args.threads
    threads = []
    print(f"[+] Generating {args.lines} lines using {args.threads} threads to '{args.output}'")
    start = time.time()

    for i in range(args.threads):
        t = threading.Thread(target=write_thread, args=(i, lines_per_thread, args.output))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    elapsed = time.time() - start
    print(f"Done. Time taken: {elapsed:.2f}s. Approx speed: {args.lines / elapsed:.2f} lines/sec")


if __name__ == '__main__':
    main()











