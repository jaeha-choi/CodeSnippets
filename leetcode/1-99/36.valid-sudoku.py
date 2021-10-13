from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        di3 = {}
        di2 = {}
        for r_idx, row in enumerate(board):
            di = set()
            for c_idx, elem in enumerate(row):
                if elem.isdigit():
                    # Checks row
                    if elem not in di:
                        di.add(elem)
                    else:
                        return False

                    # Checks box
                    keyy = str(r_idx // 3) + str(c_idx // 3)
                    di2.setdefault(keyy, [])
                    if elem not in di2[keyy]:
                        di2[keyy].append(elem)
                    else:
                        return False

                    # Checks col
                    di3.setdefault(c_idx, [])
                    if elem not in di3[c_idx]:
                        di3[c_idx].append(elem)
                    else:
                        return False
        return True
