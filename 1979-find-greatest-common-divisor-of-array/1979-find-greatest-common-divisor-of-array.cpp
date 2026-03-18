#include <iostream>
#include <limits.h>
#include <numeric>
using namespace std;

class Solution {
public:
    int min = INT_MAX;
    int max = INT_MIN;
    int findGCD(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++){
            if (nums[i]  < min){
                min = nums[i];
            }
            if (nums[i] > max){
                max = nums[i];
            }
        }
    return gcd(min, max);
    }
};