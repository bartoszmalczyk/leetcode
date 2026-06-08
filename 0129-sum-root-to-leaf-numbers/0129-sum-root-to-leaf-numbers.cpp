#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        int res = 0;
        vector<int> sol;
        
        auto dfs = [&](auto& self, TreeNode* node) -> void {
            if (!node) {
                return;
            }
            
            sol.push_back(node->val);
            
            if (!node->left && !node->right) {
                string s = "";
                for (int v : sol) {
                    s += to_string(v);
                }
                res += stoi(s);
            } else {
                self(self, node->left);
                self(self, node->right);
            }
            
            sol.pop_back();
        };
        
        dfs(dfs, root);
        
        return res;
    }
};