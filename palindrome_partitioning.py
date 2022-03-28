#Given: A string s
#Output: Return all possible palindrome partitioning of s

'''
Example:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
'''

'''
Find answer recursively and memory trick can save some time
-traverse and check every prefix s[:i] of s
-if prefix s[:i] is a palindrome, then process the left suffix s[i:] recursively
-since the suffix s[i:] may repeat, the memory trick can save some time
'''
class Solution(object):
    # @cache the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            # prefix is a palindrome
            if s[:i] == s[:i][::-1]:
                # process suffix recursively
                for suf in self.partition(s[i:]):  
                    ans.append([s[:i]] + suf)
        return ans

#s= input
#ans=[['a', 'a', 'b'], ['aa', 'b']]
#Output= [['a', 'a', 'b'], ['aa', 'b']]