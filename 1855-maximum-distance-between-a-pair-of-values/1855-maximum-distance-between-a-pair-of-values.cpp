class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int ans = 0;
        int i = 0;
        int j = 0;
        int mid = 0;
        for (int index = 0; index < nums2.size(); index++){
            i = 0;
            j = std::min(index, nums1.size() - 1)
            while (i <= j){
                mid = (i + j) / 2;
                if (nums1[mid] > nums2[index]){
                    i = mid + 1;
                }
                else{
                    ans = std::max(ans, index - mid);
                    j = mid - 1;
                }
            }
        }
        return ans;
    }
};