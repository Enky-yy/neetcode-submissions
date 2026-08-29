class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        for (int x : nums) {
            freq[x]++;
        }

        vector<pair<int, int>> counts;

        for (auto it : freq) {
            counts.push_back({it.second, it.first});
        }

        sort(counts.begin(), counts.end());

        vector<int> ans;

        for (int i = counts.size() - 1; i >= 0 && k > 0; i--, k--) {
            ans.push_back(counts[i].second);
        }

        return ans;
    }
};