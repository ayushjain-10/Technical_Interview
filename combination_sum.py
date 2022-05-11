'''Given an array of distinct integers candidates and a target integer target, 
Return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.'''

'''Example:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        def dfs(cur, cur_sum, idx):                       # try out each possible cases
            if cur_sum > target: return                   # this is the case, cur_sum will never equal to target
            if cur_sum == target: ans.append(cur); return # if equal, add to `ans`
            for i in range(idx, n): dfs(cur + [candidates[i]], cur_sum + candidates[i], i) # DFS
        dfs([], 0, 0)
        return ans   

# Straight forward backtracking
# cur: current combination, cur_sum current combination sum, idx index current at (to avoid repeats)
# Time complexity: O(N^(M/min_cand + 1)), N = len(candidates), M = target, min_cand = min(candidates)
# Space complexity: O(M/min_cand)