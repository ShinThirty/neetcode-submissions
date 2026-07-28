class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        def match(c, t):
            if t == '(':
                return c == ')'
            if t == '{':
                return c == '}'
            if t == '[':
                return c == ']'

        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st:
                    return False
                if not match(c, st[-1]):
                    return False
                st.pop()
        
        return len(st) == 0