class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }

        for t in tokens:
            if t in "+-*/":
                right = st.pop()
                left = st.pop()
                st.append(ops[t](left, right))
            else:
                st.append(int(t))
        
        return st[-1]