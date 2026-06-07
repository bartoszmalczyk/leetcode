#include <vector>
#include <algorithm>

class Solution {
public:
    int minEatingSpeed(std::vector<int>& piles, int h) {
        auto canEat = [&](int k) {
            long long hours_needed = 0; 
            for (int p : piles) {
                hours_needed += (p + k - 1) / k;
                if (hours_needed > h) {
                    return false;
                }
            }
            return true;
        };

        int l = 1;
        int r = *std::max_element(piles.begin(), piles.end());
        int ans = r;

        while (l <= r) {
            int mid = l + (r - l) / 2; 
            
            if (canEat(mid)) {
                ans = std::min(ans, mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        return ans;
    }
};