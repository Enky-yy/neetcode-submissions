class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int k = t.size();
        if(n!=k)
            return false;
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        return s==t;
    }
};
