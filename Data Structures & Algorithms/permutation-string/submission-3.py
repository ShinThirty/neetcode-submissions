class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1, m2 = Counter(), Counter()
        for c1 in s1:
            m1[c1] += 1
        n = len(s1)
        wl = 0
        l = 0
        matches = 26 - len(m1)
        for c2 in s2:
            if m2[c2] == m1[c2]:
                matches -= 1
            if m2[c2] + 1 == m1[c2]:
                matches += 1
            m2[c2] += 1
            wl += 1
            if wl > n:
                cm = s2[l]
                if m2[cm] == m1[cm]:
                    matches -= 1
                if m2[cm] -1 == m1[cm]:
                    matches += 1
                m2[cm] -= 1
                if m2[cm] == 0:
                    del m2[cm]
                l += 1
            if matches == 26:
                return True
        return False
