"""
如何从 100GB 日志中高效提取最热门 IP 地址

日志：
192.168.1.10 - - [01/Jul/2025:10:15:42 +0800] "GET /index.html HTTP/1.1" 200 1024 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - - [01/Jul/2025:10:16:01 +0800] "POST /login HTTP/1.1" 302 512 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
172.16.5.23 - - [01/Jul/2025:10:16:15 +0800] "GET /images/logo.png HTTP/1.1" 200 2048 "-" "curl/7.29.0"
192.168.1.10 - - [01/Jul/2025:10:17:42 +0800] "GET /dashboard HTTP/1.1" 200 4096 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
10.0.0.5 - - [01/Jul/2025:10:18:03 +0800] "GET /logout HTTP/1.1" 200 256 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"

"""
import utils.generate_logs

from collections import Counter

counter = Counter()

with open("utils/access.log", "r") as f:
    for line in f:
        ip = line.split()[0]
        counter[ip] += 1

for ip, count in counter.most_common(10):
    print(f"{ip}\t{count}")