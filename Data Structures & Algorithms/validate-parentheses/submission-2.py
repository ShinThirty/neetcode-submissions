class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c in "({[":
                st.append(c)
            else:
                if not st:
                    return False
                t = st.pop()
                if t == '(' and c != ')':
                    return False
                if t == '{' and c != '}':
                    return False
                if t == '[' and c != ']':
                    return False
        
        return len(st) == 0