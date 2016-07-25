class Solution {
public:
    string reverseString(string s) {
        for (int i = 0; i < s.size()/2; i++) {
            char tmp = s[s.size() - i - 1];
            s[s.size() - i - 1] = s[i];
            s[i] = tmp;
        }
        return s;
    }
};

//1Y, 12 ms, beats 28.49% of cppsubmissions, slower than java