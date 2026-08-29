class Solution {
public:
    bool isAnagram(string s, string t) {
        int n = s.size();
        int k = t.size();
        if(n!=k)
            return false;
        vector<int> count (26,0);

        for(int i = 0 ; i<n ; i++){
            count[s[i]-'a']++;
            count[t[i]-'a']--;
        }

        for(auto it : count){
            if (it!=0)
                return false;
        }

        return true;
    }
};
