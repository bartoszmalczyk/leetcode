class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int, int> hm;
        hm[0] = -1;
        int temp = 0;
        int ans = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            temp += (nums[i] == 0) ? -1 : 1;
            
            if (hm.find(temp) != hm.end()) {
                ans = std::max(ans, i - hm[temp]);
            } else {
                hm[temp] = i;
            }
        }
        
        return ans;
    }
};