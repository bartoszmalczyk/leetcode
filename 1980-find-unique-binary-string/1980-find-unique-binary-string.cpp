#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
#include <bitset>

class Solution {
public:
    std::string findDifferentBinaryString(std::vector<std::string>& nums) {
        std::unordered_set<int> nums_set;
        int n = nums[0].length();
        
        for (const std::string& bin_str : nums) {
            nums_set.insert(std::stoi(bin_str, nullptr, 2));
        }
        
        if (nums_set.find(0) == nums_set.end()) {
            return std::string(n, '0');
        }
        int min_val = *std::min_element(nums_set.begin(), nums_set.end());
        int missing_val = 0;

        for (int i = min_val; i < 65536; ++i) {
            if (nums_set.find(i) == nums_set.end()) {
                missing_val = i;
                break;
            }
        }
        
        std::string sol = std::bitset<16>(missing_val).to_string();
        
        return sol.substr(16 - n);
    }
};