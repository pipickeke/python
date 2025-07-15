"""
如何从 100GB 日志中高效提取最热门 IP 地址
"""

from collections import Counter

counter = Counter()

with open("utils/access.log","r") as f:
    for line in f:
        ip = line.split()[0]
        counter[ip] += 1

for ip, count in counter.most_common(10):
    print(f"{ip}\t{count}")


