
"""
TC: O(N * N!) {Here, N is the size of the arrangement (n), and N! is the number of possible permutations}
SC: O(N) {Here, we use a set 'used' to track which numbers are already used in the current arrangement, 
            and the recursion depth can go up to N.}

Approach:

This solution uses backtracking to count the number of beautiful arrangements possible for a given number n.

The idea is to generate all possible permutations of numbers 1 through n, while maintaining the divisibility condition:
- For each position idx (1-indexed), we check if the number placed at that position satisfies the divisibility condition:
    - The number must either be divisible by the position index (idx) or the position index must be divisible by the number.

The function performs the following steps:
1. Use backtracking to explore all possible arrangements of numbers from 1 to n.
2. At each position, we attempt to place numbers that satisfy the divisibility condition and haven't been used yet.
3. Once a valid arrangement is formed (i.e., all positions are filled), increment the result counter.

A set 'used' keeps track of which numbers have already been placed in the current arrangement, ensuring no repetition.

The recursion continues until all numbers have been placed, at which point the arrangement is valid and we count it.

This approach efficiently generates valid arrangements without generating all permutations upfront, pruning invalid paths early.

This problem has been successfully solved on platforms like Leetcode.

"""
class Solution:
    def countArrangement(self, n: int) -> int:
        def perm(idx):
            nonlocal res
            #base case
            if idx >= n:
                res += 1
                return

            #logic
            for i in range(1, n+1):
                if i not in used and (i % (idx+1) == 0 or (idx+1) % i == 0):
                    used.add(i)
                    perm(idx+1)
                    used.remove(i)
        res = 0
        used = set()
        perm(0)
        return res