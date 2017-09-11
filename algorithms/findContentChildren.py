class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        greedy = 0
        cookie = 0

        while greedy < len(g) and cookie < len(s):
            if s[cookie] >= g[greedy]:
                greedy += 1
            cookie += 1

        return greedy