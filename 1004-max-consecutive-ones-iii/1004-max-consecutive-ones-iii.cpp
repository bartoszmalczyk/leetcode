class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
       int zeros = 0;
       int l = 0, r = 0; 
       int n = nums.size();
       int ans = 0;
       
       while (r < n) { 
            if (nums[r] == 0) {
                zeros++;
            }
            
            while (zeros > k) {
                if (nums[l] == 0) {
                    zeros -= 1;
                }
                l++;
            }
            
            ans = std::max(ans, r - l + 1);
            r++;
       }
       
       return ans;
    }
};