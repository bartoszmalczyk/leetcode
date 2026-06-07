#include <string>

class Solution {
public:
    std::string intToRoman(int num) {
        std::string x = "";
        
        for (int i = 0; i < num / 1000; i++) {
            x += "M";
        }
        num = num % 1000;

        if (num / 900 != 0) { 
            x += "CM";
            num -= 900;
        }

        if (num / 500 != 0) {
            x += "D";
            num -= 500;
        }

        if (num / 400 != 0) {
            x += "CD";
            num -= 400;
        }

        for (int j = 0; j < num / 100; j++) {
            x += "C";
        }
        num = num % 100;

        if (num / 90 != 0) { 
            x += "XC";
            num -= 90;
        }

        if (num / 50 != 0) {
            x += "L";
            num -= 50;
        }

        if (num / 40 != 0) {
            x += "XL";
            num -= 40;
        }
        
        for (int j = 0; j < num / 10; j++) {
            x += "X";
        }
        num = num % 10;

        if (num / 9 != 0) { 
            x += "IX";
            num -= 9;
        }

        if (num / 5 != 0) {
            x += "V";
            num -= 5;
        }

        if (num / 4 != 0) {
            x += "IV";
            num -= 4;
        }

        for (int j = 0; j < num; j++) {
            x += "I";
        }
        
        return x;
    }
};