class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        int vectorSize = nums.size();
        bool increasing = (nums[0] < nums.back());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (increasing){
                if(nums[i + 1] < nums[i]){return false;}
            }
            else{
                if (nums[i + 1] > nums[i]{return false}
            }

        }
        return true;
    }
};