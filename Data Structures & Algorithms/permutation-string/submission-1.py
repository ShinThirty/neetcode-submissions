class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1, m2 = Counter(), Counter()
        for c1 in s1:
            m1[c1] += 1
        n = len(s1)
        wl = 0
        l = 0
        for c2 in s2:
            m2[c2] += 1
            wl += 1
            if wl > n:
                cm = s2[l]
                m2[cm] -= 1
                if m2[cm] == 0:
                    del m2[cm]
                l += 1
            if m1 == m2:
                return True
        return False
