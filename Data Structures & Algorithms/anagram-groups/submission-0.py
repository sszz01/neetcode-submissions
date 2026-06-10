class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        group_a = list()
        visited = set()
        
        for i, val_i in enumerate(strs):
            if i in visited:
                continue
            visited.add(i)
            tmp = list()
            tmp.append(val_i)
            for j, val_j in enumerate(strs):
                if sorted(val_i) == sorted(val_j) and i != j and j not in visited:
                    tmp.append(val_j)
                    visited.add(j)
            group_a.append(tmp) # somehow group together
            
        
        return group_a