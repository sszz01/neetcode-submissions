class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, val_i in enumerate(nums):
            comp = target - val_i
            for j, val_j in enumerate(nums):
                if val_j == comp and i != j:
                    return [i, j]
        return None