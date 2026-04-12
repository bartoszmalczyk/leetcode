#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <climits>

using namespace std;

class Solution {
public:
    int minimumDistance(vector<int>& nums) {
        unordered_map<int, vector<int>> hm;
        int min_ = INT_MAX;
        for (int i = 0; i < nums.size(); ++i) {
            hm[nums[i]].push_back(i);
        }
        
        for (const auto& pair : hm) {
            const vector<int>& candidate = pair.second;
            
            if (candidate.size() < 3) continue;
            
            for (size_t m = 0; m < candidate.size() - 2; ++m) {
                int i = candidate[m];
                int j = candidate[m+1];
                int k = candidate[m+2];
                
                int current_dist = abs(i - j) + abs(j - k) + abs(k - i);
                min_ = min(min_, current_dist);
            }
        }
        
        if (min_ == INT_MAX) {
            return -1;
        }
        return min_;
    }
};