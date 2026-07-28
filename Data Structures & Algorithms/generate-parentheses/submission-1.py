class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        prefix = []

        def generate(o, c):
            if c == n:
                res.append("".join(prefix))
            else:
                if o < n:
                    prefix.append('(')
                    generate(o + 1, c)
                    prefix.pop()
                if o > c:
                    prefix.append(')')
                    generate(o, c + 1)
                    prefix.pop()
        
        generate(0, 0)
        return res