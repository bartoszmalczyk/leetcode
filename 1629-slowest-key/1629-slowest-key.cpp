class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        int max_ = releaseTimes[0];
        int index = 0;
        for (int i = 1; i < releaseTimes.size(); i++){
            int temp = releaseTimes[i] - releaseTimes[i-1];
            if (temp > max_){
                max_ = temp;
                index = i;
            }
            else if (temp == max_){
                if (keysPressed[i] > keysPressed[index]){
                    index = i;
                }
            }
        }
        return keysPressed[index];
    }
};