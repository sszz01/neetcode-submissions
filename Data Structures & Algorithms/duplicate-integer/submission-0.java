class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> s = new HashSet<>();
        int n = 0;

        for(int i = 0; i < nums.length; i++) {
            if(s.add(nums[i])) {
                n++;
            }
        }

        return n != nums.length;
    }
}