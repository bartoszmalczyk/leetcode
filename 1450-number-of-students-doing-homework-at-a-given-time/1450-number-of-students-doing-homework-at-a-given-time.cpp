class Solution {
public:
    int busyStudent(vector<int>& startTime, vector<int>& endTime, int queryTime) {
        int ans = 0; 
        for (int i = 0; i < startTime.size(); i++){
            int start = startTime[i];
            int end = endTime[i];
            if (start <= queryTime && queryTime <= end){
                ans++;
            }
        }
        return ans;
    }
};

