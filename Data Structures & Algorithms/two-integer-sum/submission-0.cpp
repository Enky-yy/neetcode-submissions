class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int , int>> array1;
        int n = nums.size();
        for(int i=0; i<n ; i++){
            array1.push_back({nums[i], i});
        }
        sort(array1.begin(), array1.end());
        int left = 0;
        int right = n-1;
        while(left<right){
            long long sum = array1[left].first + array1[right].first;
            if (sum == target){
                return {min(array1[left].second , array1[right].second), max(array1[left].second , array1[right].second)};
            }
            else if(sum>target){
                right--;
            }
            else{
                left++;
            }
        }
        return {-1,-1};
    }
};
