from collections import defaultdict
from collections import deque 

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = deque()
        hm = defaultdict(int)
        prev = 0 
        for process in logs:
            func_id, call_type, timestamp = process.split(":")
            func_id = int(func_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if stack:
                    hm[stack[-1]] += timestamp - prev
                stack.append(func_id)
                prev = timestamp
            else:
                hm[stack.pop()] += timestamp - prev + 1
                prev = timestamp + 1
        return list(hm.values())