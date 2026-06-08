#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        
        function<int(int, vector<int>)> dfs = [&](int i, vector<int> prev) {
            if (i == n) {
                return *min_element(prev.begin(), prev.end());
            }
            
            vector<int> x;
            vector<int> temp = {1001};
            temp.insert(temp.end(), prev.begin(), prev.end());
            temp.push_back(1001);
            
            for (int j = 0; j <= i; j++) {
                x.push_back(triangle[i][j] + min(temp[j], temp[j + 1]));
            }
            
            return dfs(i + 1, x);
        };
        
        return dfs(1, triangle[0]);
    }
};