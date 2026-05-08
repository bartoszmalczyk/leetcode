#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) {
            return {};
        }

        sort(intervals.begin(), intervals.end(), [](const vector<int>& a, const vector<int>& b) {
            return a[0] < b[0];
        });

        vector<vector<int>> merged;
        vector<int> prev = intervals[0];
        int n = intervals.size();

        for (int i = 1; i < n; ++i) {
            const vector<int>& curr = intervals[i]; 
            
            if (prev[1] >= curr[0]) { 
                prev[1] = max(prev[1], curr[1]);
            } else {
                merged.push_back(prev);
                prev = curr;
            }
        }
        
        merged.push_back(prev);
        return merged;
    }
};