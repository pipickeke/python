from collections import Counter
from typing import List


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = Counter(students)
        for i, x in enumerate(sandwiches):
            if cnt[x] == 0:
                return len(sandwiches) - i
            cnt[x] -= 1
        return 0
