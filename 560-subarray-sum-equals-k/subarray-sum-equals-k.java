class Solution {
    public int subarraySum(int[] nums, int k) {
        int total = 0;
        int p = 0;
        int n = nums.length;
        
        for (int i = 0; i < n; i++) {
            int rem = k;
            p = i;
            while (p < n) {
                rem = rem - nums[p];
                if (rem == 0) total++;
                p++;
            }
        }
        
        return total;
    }
}