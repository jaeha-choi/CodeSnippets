from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit = []
        d = {}
        for log in logs:
            ln = log.split()
            if ln[1].isdigit():
                digit.append(log)
            else:
                d.setdefault(log[len(ln[0]):], [])
                d[log[len(ln[0]):]].append(ln[0])

        s = []
        for key in sorted(d.keys()):
            for tag in sorted(d[key]):
                s.append(tag + key)
        s.extend(digit)
        return s
