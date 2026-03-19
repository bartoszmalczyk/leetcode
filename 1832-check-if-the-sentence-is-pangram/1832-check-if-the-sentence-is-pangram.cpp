#include <string>
#include <unordered_set>

class Solution {
public:
    bool checkIfPangram(std::string sentence) {
        std::unordered_set<char> temp;
        for (char c : sentence) {
            temp.insert(c);
        }
        return temp.size() == 26;
    }
};