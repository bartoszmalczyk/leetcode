using namespace std;

class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        int n = words.size();
        
        if (words[startIndex] == target) {
            return 0;
        }

        for (int i = 1; i < n; ++i) {
            string l = words[(startIndex - i + n) % n];
            string r = words[(startIndex + i) % n];

            if (l == target || r == target) {
                return i;
            }
        }
        return -1;
    }
};