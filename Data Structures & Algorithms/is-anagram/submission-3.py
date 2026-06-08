class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map, t_map = dict(), dict()

        for i in s:
            s_map[i] = 0
        
        for j in t:
            t_map[j] = 0
        
        for char in s:
            s_map[char] += 1
        
        for char in t:
            t_map[char] += 1
        
        return s_map == t_map