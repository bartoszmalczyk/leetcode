#include <vector>

using namespace std;

class Solution {
public:
    int equalPairs(vector<vector<int>>& grid) {
        int n = grid[0].size();
        vector<int> temp;
        int res = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                temp.push_back(grid[j][i]);
            }
            for (const auto& k : grid) {
                if (k == temp) {
                    res += 1;
                }
            }
            temp.clear();
        }
        
        return res;
    }
};