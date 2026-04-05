using namespace std;

class Solution {
public:
    bool judgeCircle(string moves) {
        int vertical = 0;
        int horizontal = 0;
        char symbol;
        for (int i = 0; i < moves.size(); i++){
            symbol = moves[i];
            if (symbol == 'U'){ 
                vertical++;
            }
            else if (symbol == 'D'){
                vertical--;
            }
            else if (symbol == 'R'){
                horizontal++;
            }
            else{
                horizontal--;
            }
        }
        if (vertical == 0 && horizontal == 0){
            return true;
        }
        return false;
    }
};