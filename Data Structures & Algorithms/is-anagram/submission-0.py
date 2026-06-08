class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for i, val in enumerate(s):
            if val in s_map:
                s_map[val] += 1
            else:
                s_map[val] = 1
        print(s_map)

        for i, val in enumerate(t):
            if val in t_map:
                t_map[val] += 1
            else:
                t_map[val] = 1
        print(t_map)

        return s_map == t_map