from typing import List


class Solution:

    # Shares the same idea as Approach 2, but I've used .copy() instead of using .pop().
    # Using pop() allows us not to use .copy() and other variables to keep track of "(".
    #     def generateParenthesis(self, n: int) -> List[str]:
    #         li = []
    #         def helper(stack, elem, opn_cnt, opn_remain):
    #             stack.append(elem)
    #             if opn_cnt < n and len(stack) < n * 2 -1:
    #                 new = stack.copy()
    #                 helper(new, "(", opn_cnt + 1, opn_remain+1)
    #             if opn_remain > 0 and len(stack) < n * 2:
    #                 helper(stack,")", opn_cnt, opn_remain - 1)
    #             if opn_remain == 0 and opn_cnt == n:
    #                 li.append("".join(stack))
    #         helper([], "(", 1, 1)
    #         return li

    def generateParenthesis(self, n: int) -> List[str]:
        li = []

        def helper(stack, elem, opn_cnt, opn_remain):
            stack.append(elem)

            if opn_cnt < n and len(stack) < n * 2 - 1:
                helper(stack, "(", opn_cnt + 1, opn_remain + 1)
                stack.pop()

            if opn_remain > 0 and len(stack) < n * 2:
                helper(stack, ")", opn_cnt, opn_remain - 1)
                stack.pop()

            if opn_remain == 0 and opn_cnt == n:
                li.append("".join(stack))

        helper([], "(", 1, 1)
        return li
