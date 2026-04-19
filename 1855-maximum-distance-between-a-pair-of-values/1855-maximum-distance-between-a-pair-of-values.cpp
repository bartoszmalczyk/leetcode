class Solution {
public:
    int maxDistance(std::vector<int>& nums1, std::vector<int>& nums2) {
        int ans = 0;
        int n1 = nums1.size(); 
        
        for (int index = 0; index < nums2.size(); index++) {
            int i = 0;
            int j = std::min(index, n1 - 1); 
            while (i <= j) {
                int mid = i + (j - i) / 2; 
                
                if (nums1[mid] > nums2[index]) {
                    i = mid + 1;
                } else {
                    ans = std::max(ans, index - mid);
                    j = mid - 1;
                }
            }
        }
        return ans;
    }
};