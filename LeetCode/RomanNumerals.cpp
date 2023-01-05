class Solution {
public:
    int romanToInt(string s) {
        int result = 0;
        for(int i = s.length(); i >=0; i--) {
            if(i == s.length()) {
                result += charToInt(s[i]);
            } else if(charToInt(s[i]) < charToInt(s[i+1])) {
                result -= charToInt(s[i]);
            } else {
                result += charToInt(s[i]);
            }
        }
        return result;
    }

    int charToInt(char c) {
        if(c == 'M') return 1000;
        if(c == 'D') return 500;
        if(c == 'C') return 100;
        if(c == 'L') return 50;
        if(c == 'X') return 10;
        if(c == 'V') return 5;
        if(c == 'I') return 1;
        return 0;
    }
};