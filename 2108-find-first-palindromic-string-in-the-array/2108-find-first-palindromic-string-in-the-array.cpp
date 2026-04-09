#include <string>
using namespace std;
class Solution {
public:
    string firstPalindrome(vector<string>& words) {
        bool isPalindromic(string s){
            int l = 0;
            int r = s.size() - 1;
            while (l <= r){
                if (s[l] != s[r]){return false;}
                l++;
                r--;
            }
            return true
        }
        for (int i = 0; i < words.size(); i++){
            if (isPalindromic(words[i])){
                return words[i];
            }
        }
        return "";
    }
};